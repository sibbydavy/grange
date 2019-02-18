#from FlaskWebProject1.DTOs.YieldPeriodMaster import YieldPeriodMaster
class CropMaster(object):
    def __init__(self):
        self._cropCode = ""
        self._cropName = ""
        self._yieldPeriodMaster = []

    @property #code
    def code(self):
     return self._code 
    @code.setter
    def code(self, value):
     self._code = value

    @property #cropName
    def cropName(self):
     return self._cropName 
    @cropName.setter
    def cropName(self, value):
     self._cropName = value

    @property #expenseMaster
    def yieldPeriodMaster(self):
     return self._yieldPeriodMaster
    @yieldPeriodMaster.setter
    def yieldPeriodMaster(self, value):
     self._yieldPeriodMaster = value

    def getRecord(self, code):
      self._code = code #"c1"
      self._cropName = "elanchi" 
      print("crop")
      #for x in range(2):
      #  record = YieldPeriodMaster()
      #  self.yieldPeriodMaster[x] = record.getRecord(1)  
      return self 


