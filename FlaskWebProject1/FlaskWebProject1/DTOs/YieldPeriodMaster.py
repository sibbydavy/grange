from FlaskWebProject1.DTOs.WorkersExpense import WorkersExpense
from FlaskWebProject1.DTOs.ProductExpense import ProductExpense
class YieldPeriodMaster(object):
  def __init__(self):
    self._code = ""
    self._description = ""
    self._periodName = ""
    self._periodStart = ""
    self._periodEnd  = ""    
    self._isCurrent = 0
    self._workersExpense = {}
    self._productExpense = {}

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

  @property #periodName
  def periodName(self):
      return self._periodName 
  @periodName.setter
  def periodName(self, value):
      self._periodName = value

  @property #periodStart
  def periodStart(self):
      return self._periodStart 
  @periodStart.setter
  def periodStart(self, value):
      self._periodStart = value

  @property #periodEnd
  def periodEnd(self):
      return self._periodEnd
  @periodEnd.setter
  def periodEnd(self, value):
      self._periodEnd = value

  @property #workersExpense
  def workersExpense(self):
      return self._workersExpense
  @workersExpense.setter
  def workersExpense(self, value):
      self._workersExpense = value

  @property #productExpense
  def productExpense(self):
      return self._productExpense
  @productExpense.setter
  def productExpense(self, value):
      self._productExpense = value

  def getRecord(self, code):
      self._code = "1"
      self._description = "Initial period"
      self._periodName = "Period 1"
      self._periodStart = "01/07/2018"
      self._periodStart = "01/07/2018"
      self._amount = amount
      self._paidBy = paidBy
       
      for x in range(2):
          record = WorkersExpense()
          self._expenseMaster[x] = record.getRecord(1)            
          self._expenseMaster[x] =record

      for x in range(2):
          record = ProductExpense()
          self._productExpense[x] = record.getRecord(1)            
          self._productExpense[x] =record

      return self 
