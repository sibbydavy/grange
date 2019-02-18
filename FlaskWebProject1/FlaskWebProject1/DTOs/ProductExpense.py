from FlaskWebProject1.DTOs.ExpenseMaster import ExpenseMaster
class ProductExpense(object):
  def __init__(self):
    self._code = ""
    self._description = ""
    self._qty = 0.000
    self._uom = ""
    self._price = 0.00
    self._tax = 0.00
    self._total = 0.00
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

  @property #qty
  def qty(self):
      return self._qty 
  @qty.setter
  def qty(self, value):
      self._qty = value

  @property #uom
  def uom(self):
      return self._uom 
  @uom.setter
  def uom(self, value):
      self._uom = value

  @property #price
  def price(self):
      return self._price 
  @price.setter
  def price(self, value):
      self._price = value

  @property #tax 
  def tax(self):
      return self._tax 
  @tax.setter
  def tax(self, value):
      self._tax = value

  @property #total 
  def total(self):
      return self._total 
  @total.setter
  def total(self, value):
      self._total = value


  @property #expenseMaster
  def expenseMaster(self):
      return self._expenseMaster
  @expenseMaster.setter
  def expenseMaster(self, value):
      self._expenseMaster = value

  def getRecord(self, code):
      self._code = code #"p1"
      self._description = "buy pesticides"
      self._qty = 5  
      self._uom = "kg"
      self._price = 100.00
      self._tax = 10
      self._total = 110
      for x in range(2):
          record = ExpenseMaster()
          self._expenseMaster[x] = record.getExpenseMaster(1)            
          self._expenseMaster[x] =record
      return self 





