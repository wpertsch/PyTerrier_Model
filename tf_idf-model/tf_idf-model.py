import pyterrier as pt
pt.init()

def indexing():
   files = pt.io.find_files("/home/bm3302/ArqMath_Task1/")
   indexer = pt.TRECCollectionIndexer("./wt2g_index", verbose=True, blocks=False, overwrite=True)
   indexer.setProperty("max.term.length", "20")
   indexer.setProperty("tokeniser", "UTFTokeniser")
   indexer.setProperty("FieldTags.process", "TITLE")
   indexer.setProperty("TrecDocTags.doctag", "DOC")
   indexer.setProperty("TrecDocTags.idtag", "DOCNO")
   indexref = indexer.index(files)
   index = pt.IndexFactory.of(indexref)