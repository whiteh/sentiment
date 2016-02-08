import web
import json
import mimerender
import string
import pickle
import sys

sys.path.append('../model')
sys.path.append('../process')
from NLTKpipeline import NLTKpipeline
from document import document

mimerender = mimerender.WebPyMimeRender()

f = open('../my_classifier.pickle', 'rb')
classifier = pickle.load(f)
f.close()

render_xml = lambda message: '<message>%s</message>'%message
render_json = lambda **args: json.dumps(args)
render_html = lambda message: '<html><body>%s</body></html>'%message
render_txt = lambda message: message

process = NLTKpipeline()

urls = (
    '/(tweet)', 'tweetClassify'
)
app = web.application(urls, globals())

def preprocess(sent):
    doc = document()
    doc.setText(sent)
    process.processDoc(doc)
    return doc.toVector()[0]

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