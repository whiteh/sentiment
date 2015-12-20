from document import document
import re

class csvExtractor:
  def __init__(self, text_col=None, label_col=None, label_const = None, delim_patt=None):
    self.text_col    = text_col
    self.label_col   = label_col
    self.label_const = label_const
    self.delim_patt  = delim_patt

  def setLabelDictionary(self, label_dict):
    self.label_dict = label_dict

  def clean(self, st):
    st = re.sub(self.delim_patt, "", st)
    return st

  def run(self, line):
    parts = line.split(",")
    doc = document()
    doc.setText(parts[self.text_col])

    if (self.label_const == None):
      doc.setLabel(self.label_dict[self.clean(parts[self.label_col])])
    else:
      doc.setLabel(self.label_const)
    doc.setText(self.clean(parts[self.text_col]))
    return doc

class corpus:
  def __init__(self, loc = None, extractor=None):
    self.docs      = []
    self.loc       = loc
    self.extractor = extractor
    if (self.loc != None and self.extractor !=None):
      try:
        self.load()
      except Exception as e:
        print "Exception in load: "+str(e)

  def load(self, loc=None, extractor = None):
    if (self.loc == None and loc == None):
      raise Exception("No location set")
    if (self.extractor == None and extractor == None):
      raise Exception("No extractor set")
    self.loadFromFile()

  def loadFromFile(self):
    count = 0
    f = self.openFile()
    for line in f:
      item = self.extractor.run(line)
      self.docs.append(item)
      count+=1
    print str(count)+" documents loaded: "+str(len(self.docs))+" in collection..."

  def openFile(self):
    if self.loc == None:
      raise Exception("No file source set")
    try:
      f = open(self.loc, "r")
      print self.loc+" opened..."
      return f
    except Exception as e:
      raise e;

  def each(self, callback):
    for a in self.docs:
      callback(a)

def runTests():
  extractor = csvExtractor(label_col=0,text_col=4, delim_patt='"')
  extractor.setLabelDictionary({"0":"pos", "4":"neg"})
  c = corpus(loc="/home/nitrous/data/sentiment140/training.1600000.processed.noemoticon.csv", extractor=extractor)

if __name__ == "__main__":
  runTests()