import FlaskWebProject1.CropMaster
class FarmMasterDetailX(object):
  def __init__(self, farmCode, farmName):
    self._farmCode = farmCode
    self._farmName = farmName
    self._cropSummary =[]

  @property
  def farmCode(self):
      return self._farmCode 

  @farmCode.setter
  def farmCode(self, value):
      self._farmCode = value

  @property
  def farmName(self):
      return self._farmName 

  @farmName.setter
  def farmName(self, value):
      self._farmName = value


  @property #CROP Summary
  def cropSummary(self):
      return self._cropSummary

  @cropSummary.setter
  def cropSummary(self, value):
      self._cropSummary = value

  def getFarmDetail(self):
        self._farmCode = "f#1"
        self._farmName = "farm sample 1"
        #self._monster = FlaskWebProject1.CropMaster(1,"apple") 
        #self._monster  = {1: 'apple', 2: 'organe'}
        self._cropSummary = {1: 'apple', 2: 'organe'}
        return self 
