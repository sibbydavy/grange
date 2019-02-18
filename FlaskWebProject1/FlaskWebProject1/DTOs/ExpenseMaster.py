class ExpenseMaster(object):
  def __init__(self):
    self._code = ""
    self._description = ""
    self._dateOfEntry = ""
    self._dateOfExp = ""
    self._amount = 0    
    self._paidBy = ""
    #self._periodCode = ""
    #self._accountType = ""
    #self._refCode = ""

  @property #code
  def code(self):
      return self._code 
  @code.setter
  def code(self, value):
      self._code = value

  @property #description
  def description(self):
      return self._description 
  @description.setter
  def name(self, value):
      self._description = value

  @property #dateOfEntry
  def dateOfEntry(self):
      return self._dateOfEntry 
  @dateOfEntry.setter
  def name(self, value):
      self._dateOfEntry = value

  @property #dateOfExp
  def dateOfExp(self):
      return self._dateOfExp 
  @dateOfExp.setter
  def dateOfExp(self, value):
      self._dateOfExp = value

  @property #amount
  def amount(self):
      return self._amount 
  @amount.setter
  def amount(self, value):
      self._amount = value

  @property #paidBy
  def paidBy(self):
      return self._paidBy 
  @paidBy.setter
  def paidBy(self, value):
      self._paidBy = value

  #@property #accountType
  #def accountType(self):
  #    return self._accountType 

  #@accountType.setter
  #def accountType(self, value):
  #    self._accountType = value

  #@property #refCode
  #def refCode(self):
  #    return self._refCode 

  #@refCode.setter
  #def refCode(self, value):
  #    self._refCode = value

  def getRecord(self, code):
      self._code = code #"1"
      self._description = "motor purchase"
      self._dateOfEntry = "13/05/2019"
      self._dateOfExp = "12/05/2019"
      self._amount = amount
      self._paidBy = paidBy
      #self._periodCode = ""
      #self._accountType = ""
      #self._refCode = ""
      return self 



