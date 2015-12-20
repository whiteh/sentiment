import sys
sys.path.append('./model')
sys.path.append('./process')
sys.path.append('./training')
sys.path.append('./service')
from corpus import corpus
from corpus import csvExtractor
from NLTKpipeline import NLTKpipeline

extractor = csvExtractor(label_col=0,text_col=5, delim_patt='"')
extractor.setLabelDictionary({"0":"pos", "4":"neg"})
c = corpus(loc="/home/nitrous/data/sentiment140/subset.csv", extractor=extractor)

pipeline = NLTKpipeline()
pipeline.process(c)

for a in c.docs:
  a.toString()
  print "\n"



