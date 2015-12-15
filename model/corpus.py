from document import document
import re

class csvExtracter:
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

class corpus:
  def __init__(self, loc = None, extracter=None):
    self.docs      = []
    self.loc       = loc
    self.extracter = extracter
    if (self.loc != None and self.extracter !=None):
      try:
        self.load()
      except Exception as e:
        print "Exception in load: "+str(e)

  def load(self, loc=None, extracter = None):
    if (self.loc == None and loc == None):
      raise Exception("No location set")
    if (self.extracter == None and extracter == None):
      raise Exception("No extracter set")
    self.loadFromFile()

  def loadFromFile(self):
    count = 0
    f = self.openFile()
    for line in f:
      item = self.extracter.run(line)
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

extracter = csvExtracter(label_col=0,text_col=4, delim_patt='"')
extracter.setLabelDictionary({"0":"pos", "4":"neg"})
c = corpus(loc="/home/nitrous/data/sentiment140/training.1600000.processed.noemoticon.csv", extracter=extracter)