import pyterrier as pt
import csv
pt.init()

def testingindex():
   files = pt.io.find_files("/home/wilhelm/Uni/retrievalsystem/beispielretrieval/indexbeispiel/")
   indexer = pt.TRECCollectionIndexer("./wt2g_index", verbose=True, blocks=False, overwrite=True)
   indexer.setProperty("max.term.length", "20")
   indexer.setProperty("tokeniser", "UTFTokeniser")
   indexer.setProperty("FieldTags.process", "TITLE")
   indexer.setProperty("TrecDocTags.doctag", "DOC")
   indexer.setProperty("TrecDocTags.idtag", "DOCNO")
   indexref = indexer.index(files)
   index = pt.IndexFactory.of(indexref)
   di = index.getDirectIndex()
   doi = index.getDocumentIndex()
   lex = index.getLexicon()
   docid = 0  # docids are 0-based
   # NB: postings will be null if the document is empty
   for posting in di.getPostings(doi.getDocumentEntry(docid)):
      termid = posting.getId()
      lee = lex.getLexiconEntry(termid)
      print("%s with frequency %d" % (lee.getKey(), posting.getFrequency()))

   tf_idf_retrieval = pt.BatchRetrieve(index, wmodel="TF_IDF", properties={"tokeniser": "UTFTokeniser"})
   res = tf_idf_retrieval.search("Database")
   pt.io.write_results(res, "tf_idf_results.res")

def testingretrieval():
   files = pt.io.find_files("/home/wilhelm/Uni/retrievalsystem/beispielretrieval/retrivalbeispiel/")
   indexer = pt.TRECCollectionIndexer("./wt2g_index", verbose=True, blocks=False, overwrite=True)
   indexer.setProperty("max.term.length", "20")
   indexer.setProperty("tokeniser", "UTFTokeniser")
   indexer.setProperty("FieldTags.process", "TITLE")
   indexer.setProperty("TrecDocTags.doctag", "DOC")
   indexer.setProperty("TrecDocTags.idtag", "DOCNO")
   indexref = indexer.index(files)
   index = pt.IndexFactory.of(indexref)
   di = index.getDirectIndex()
   doi = index.getDocumentIndex()
   lex = index.getLexicon()
   docid = 1  # docids are 0-based
   # NB: postings will be null if the document is empty
   for posting in di.getPostings(doi.getDocumentEntry(docid)):
      termid = posting.getId()
      lee = lex.getLexiconEntry(termid)
      print("%s with frequency %d" % (lee.getKey(), posting.getFrequency()))

   tf_idf_retrieval = pt.BatchRetrieve(index, wmodel="TF_IDF", properties={"tokeniser": "UTFTokeniser"})
   res = tf_idf_retrieval.search("Database Index")
   pt.io.write_results(res, "tf_idf_results.res")

if __name__ == '__main__':
   testingretrieval()
   testingindex()