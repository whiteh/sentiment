class document:
  def __init__(self):
    self.params = {}
    self.addParam("text", "")
    self.addParam("label", "")

  def setText(self, text):
    self.addParam("text", text)

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

  def toString(self):
    for a in self.listParams():
      print a + " => "+str(self.params.get(a))