from pipeline import pipeline
import nltk
from nltk.corpus import stopwords
import string
import re

class NLTKpipeline(pipeline):
  def __init__(self):
    super(NLTKpipeline, self).__init__()
    self.addPhase(twitterPhase())
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


class twitterPhase:

  def getMentions(self, text):
    regex = re.compile("(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9]+)")
    return regex.findall(text)

  def getHashtags(self, text):
    regex = re.compile("#\\w*")
    return regex.findall(text)

  def getURLs(self, text):
    regex = re.compile('[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)')
    return regex.findall(text)

  def run(self, doc):
    text = doc.getParam("text")
    doc.addParam("hashtags", self.getHashtags(text))
    doc.addParam("urls", self.getURLs(text))
    doc.addParam("mentions", self.getMentions(text))



def runTests():
  nltk = NLTKpipeline()
  nltk.toString()

if __name__ == "__main__":
  runTests();