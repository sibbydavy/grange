class PersonalAccount(object):
  def __init__(self):
    self._code = ""
    self._name = ""

  @property #code
  def code(self):
      return self._code 

  @code.setter
  def code(self, value):
      self._code = value

  @property #name
  def name(self):
      return self._name 

  @name.setter
  def name(self, value):
      self._name = value

  def getPersonalAccount(self):
        self._code = 1
        self._name = "Rogy"
        return self 
