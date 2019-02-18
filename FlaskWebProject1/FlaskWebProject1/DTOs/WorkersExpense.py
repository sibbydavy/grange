from FlaskWebProject1.DTOs.ExpenseMaster import ExpenseMaster
class WorkersExpense(object):
  def __init__(self):
    self._code = ""
    self._description = ""
    self._numberOfEmp = 0
    self._empType = ""
    self._expenseMaster = []

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
  def description(self, value):
      self._description = value

  @property #numberOfEmp
  def numberOfEmp(self):
      return self._numberOfEmp 
  @numberOfEmp.setter
  def numberOfEmp(self, value):
      self._numberOfEmp = value

  @property #empType
  def empType(self):
      return self._empType 
  @empType.setter
  def empType(self, value):
      self._empType = value

  @property #expenseMaster
  def expenseMaster(self):
      return self._expenseMaster
  @expenseMaster.setter
  def expenseMaster(self, value):
      self._expenseMaster = value

  def getRecord(self, code):
      self._code = code #"w1"
      self._description = "10 workers for plant maitenance"
      self._numberOfEmp = 10       
      for x in range(2):
          record = ExpenseMaster()
          self._expenseMaster[x] = record.getRecord(1)            
          self._expenseMaster[x] =record
      return self 


