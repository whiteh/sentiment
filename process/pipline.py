class pipeline:
  def __init__(self):
    self.stages = []

  def addPhase(self, phase, position=None):
    if (position == None):
      self.stages.append(phase)
      return
    else:
      if ( (position-1) == len(self.stages) ):
        self.stages.append(phase)
        return
      elif ((position-1) > len(self.stages)):
        a = len(self.stages)
        while ( a < (position-1) ):
          self.stages.append(None)
          a+=1
      self.stages.insert(position, phase)

## Tests
def test(testname, cond):
  if ( cond == True ):
    print testname+": OK"
  else:
    print testname+": NOK **"



pipe = pipeline()
pipe.addPhase("phase 1") ## append first item
test("first phase - len", len(pipe.stages)==1)
test("first phase - success", pipe.stages[0]=="phase 1")

pipe.addPhase("phase 2", 1)  ## should be equal to append
test("second phase - len", len(pipe.stages)==2)
test("second phase - appended", pipe.stages[1]=="phase 2")

pipe.addPhase("phase 3", 1)  ## insert between items
test("third phase - len", len(pipe.stages)==3)
test("third phase - inserted", (pipe.stages[1]=="phase 3" and pipe.stages[2]=="phase 2"))

pipe.addPhase("phase 4", 6)  ## fill in with None
test("four phase - len", len(pipe.stages)==6)
test("four phase - filled in list", (pipe.stages[3]==None and pipe.stages[5]=="phase 4"))


# for a in pipe.stages:
#   print a
