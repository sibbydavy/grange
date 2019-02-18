class CropMaster(object):
    def __init__(self, cropCode, cropName):
        self._cropCode = cropCode;
        self._cropName = cropName;

        @property #CROP CODE
        def cropCode(self):
            return self._cropCode 

        @cropCode.setter
        def cropCode(self, value):
            self._cropCode = value

        @property #CROP NAME
        def cropName(self):
            return self._cropName 

        @cropName.setter
        def cropName(self, value):
            self._cropName = value



    def GetCropDetail(self):
     return self 


