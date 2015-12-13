import web
import json
import mimerender
import nltk
from nltk.corpus import stopwords
import string
import pickle

mimerender = mimerender.WebPyMimeRender()
stop = stopwords.words('english') + [i for i in string.punctuation]
wnl = nltk.WordNetLemmatizer()

f = open('../training/my_classifier.pickle', 'rb')
classifier = pickle.load(f)
f.close()

render_xml = lambda message: '<message>%s</message>'%message
render_json = lambda **args: json.dumps(args)
render_html = lambda message: '<html><body>%s</body></html>'%message
render_txt = lambda message: message

urls = (
    '/(tweet)', 'tweetClassify'
)
app = web.application(urls, globals())

def preprocess(sent):
      tokens  = [i for i in nltk.word_tokenize(sent.lower()) if i not in stop]
      lemmatised = [wnl.lemmatize(t) for t in tokens]
      index = dict.fromkeys(set(lemmatised), 0)
      for b in lemmatised:
        index[b] += 1.0
      return index

class greet:
    @mimerender(
        default = 'html',
        html = render_html,
        xml  = render_xml,
        json = render_json,
        txt  = render_txt
    )
    def GET(self, name):
        if not name:
            name = 'world'
        return {'message': 'Hello, ' + name + '!'}

class tweetClassify:
    @mimerender(
        default = 'html',
        html = render_html,
        xml  = render_xml,
        json = render_json,
        txt  = render_txt
    )


    def GET(self, name):
        if not name:
            name = 'world'
        return {'message': 'Hello, ' + name + '!'}

    def POST(self, name):
      i = json.loads(web.data())
      print i
      if "text" not in i:
        return {'message': "error"}
      else:
        b = unicode(i["text"])
        print b
        b = preprocess(b)
        b = classifier.classify(b)
        print b
        return "{\"message\": \""+str(b)+"\"}"


if __name__ == "__main__":
    app.run()