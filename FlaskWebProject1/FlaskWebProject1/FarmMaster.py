
class FarmMasterDetail:
  def __init__(self, farmCode):
    self._farmCode = farmCode;

    @property
    def farmCode(self):
        return self._farmCode 

    @farmCode.setter
    def farmCode(self, value):
        self._farmCode = value

  def myfunc(self):
    return self 
