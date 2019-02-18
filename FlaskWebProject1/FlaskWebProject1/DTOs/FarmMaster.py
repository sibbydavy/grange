from FlaskWebProject1.DTOs.CropMaster import CropMaster
class FarmDetail(object):
    def __init__(self):
        self._farmCode = ""
        self._farmName = ""
        self._cropMaster = []

    @property #code
    def farmCode(self):
        return self._farmCode 
    @farmCode.setter
    def farmCode(self, value):
        self._farmCode = value

    @property #farmName
    def farmName(self):
        return self._farmName 
    @farmName.setter
    def farmName(self, value):
        self._farmName = value

    @property #cropMaster
    def cropMaster(self):
        return self._cropMaster 
    @cropMaster.setter
    def cropMaster(self, value):
        self._cropMaster = value


    def getRecord(self, code):
        self._farmCode = code #"f1"
        self._farmName = "iduki" 
        print("in farm")
        #self._cropMaster = {1: 'apple', 2: 'organe'}
        obj = CropMaster()
        for x in range(2):           
            record = obj.getRecord("c1") 
            print("inside crop loop")
            print(record.cropName)
            self._cropMaster.append(record)# record.getRecord("c1")            
        return self 

