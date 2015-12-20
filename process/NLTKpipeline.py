from pipeline import pipeline
import nltk
from nltk.corpus import stopwords
import string

class NLTKpipeline(pipeline):
  def __init__(self):
    super(NLTKpipeline, self).__init__()
    self.addPhase(tokenisationPhase())
    self.addPhase(lemmatisationPhase())


class tokenisationPhase:
  def __init__(self):
    self.stop = stopwords.words('english') + [i for i in string.punctuation]

  def run(self, doc):
    sent = doc.getParam("text")
    tokens  = [i for i in nltk.word_tokenize(sent.lower()) if i not in self.stop]
    doc.addParam("tokens", tokens)
    #return doc

class lemmatisationPhase:
  def __init__(self):
    self.wnl = nltk.WordNetLemmatizer()

  def run(self, doc):
    tokens = doc.getParam("tokens")
    if tokens != None:
      lemmatised = [self.wnl.lemmatize(t) for t in tokens]
      doc.addParam("lemmas", lemmatised)
    else:
      raise "Lemmatisation before tokenisation error"




def runTests():
  nltk = NLTKpipeline()
  nltk.toString()

if __name__ == "__main__":
  runTests();