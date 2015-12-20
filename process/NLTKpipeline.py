from pipeline import pipeline
import nltk
from nltk.corpus import stopwords
import string

class NLTKpipeline(pipeline):
  def __init__(self):
    super(NLTKpipeline, self).__init__()
    self.addPhase(tokenisationPhase())


class tokenisationPhase:
  def __init__(self):
    self.stop = stopwords.words('english') + [i for i in string.punctuation]

  def run(self, doc):
    tokens  = [i for i in nltk.word_tokenize(sent.lower()) if i not in self.stop]
    doc.addParam("tokens", tokens)

def runTests():
  nltk = NLTKpipeline()
  nltk.toString()
  

if __name__ == "__main__":
  runTests();