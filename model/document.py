class document:
  def __init__(self):
    self.params = {}
    self.addParam("text", "")
    self.addParam("label", "")

  def setText(self, text):
    self.addParam("text", unicode(text))

  def setLabel(self, label):
    self.addParam("label", label)

  def addParam(self, param, value):
    self.params[param]=value

  def getParam(self, param):
    if param in self.params:
      return self.params.get(param)
    else:
      return None

  def listParams(self):
    return self.params.keys()

  def toVector(self):
    vec = dict()
    l = self.listParams()
    l.remove("label")
    for a in l:
      par = self.getParam(a)
      if (isinstance(par, list)):
        for b in par:
          key = a.lower()+"_"+b.lower()
          if (key in vec):
            vec[key]+=1
          else:
            vec[key]=1
    #if ("label" in self.listParams()):
    #  vec["label"] = self.getParam("label")
    return (vec, self.getParam("label"))

  def toString(self):
    for a in self.listParams():
      print a + " => "+str(self.params.get(a))