import pyterrier as pt
from os import path
import csv
pt.init()

def testingindex():
   print("This is the index test:\n"
         "The following output are the tokenized and stemmed terms of the document:\n"
         "What are all the homomorphisms between the rings &lt;span class=&quot;math-container&quot; \n"
         "id=&quot;3019&quot;&gt;\mathbb{Z}_{18}&lt;/span&gt; and &lt;span class=&quot;math-container&quot; \n"
         "id=&quot;3020&quot;&gt;\mathbb{Z}_{15}&lt;/span&gt;?\n \n")
   basepath = path.dirname(__file__)
   filepath = path.abspath(path.join(basepath,"indexbeispiel"))
   files = pt.io.find_files(filepath)
   indexer = pt.TRECCollectionIndexer("./index_for_indextesting", blocks=False, overwrite=True)
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


def testingretrieval():
   print("\n"
         "This is testingretrieval:?\n"
         "Creates a scoring of the documents in retrievalbeispiel/retrievalbeispieldokumente in testingretrieval.res")
   basepath = path.dirname(__file__)
   filepath = path.abspath(path.join(basepath, "retrievalbeispiel"))
   files = pt.io.find_files(filepath)
   indexer = pt.TRECCollectionIndexer("./index_for_retrievaltesting", blocks=False, overwrite=True)
   indexer.setProperty("max.term.length", "20")
   indexer.setProperty("tokeniser", "UTFTokeniser")
   indexer.setProperty("FieldTags.process", "TITLE")
   indexer.setProperty("TrecDocTags.doctag", "DOC")
   indexer.setProperty("TrecDocTags.idtag", "DOCNO")
   indexref = indexer.index(files)
   index = pt.IndexFactory.of(indexref)
   tf_idf_retrieval = pt.BatchRetrieve(index, wmodel="TF_IDF", properties={"tokeniser": "UTFTokeniser"})
   res = tf_idf_retrieval.search("Database Index")
   pt.io.write_results(res, "testingretrieval.res")
