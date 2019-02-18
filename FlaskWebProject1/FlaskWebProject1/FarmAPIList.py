from datetime import datetime
from flask import render_template, jsonify
from FlaskWebProject1 import app
from FlaskWebProject1.DTOs.FarmMaster import FarmDetail
#import FlaskWebProject1.SampleDTO
from FlaskWebProject1.DTOs.SampleSerializeObjejct import MobilePhoneEncoder
from FlaskWebProject1.DTOs.SampleSerializeObjejct import MobilePhone
import json



@app.route('/todo/api/v1.0/farms', methods=['GET'])
def get_farmsB():
    x = FlaskWebProject1.FarmMaster.FarmMasterDetail('f#1',"farm sample") 
    crops = []
    #for val in x._cropSummary:   

    tasks = [
    {
        'id': x._farmCode,
        'farm name':x._farmName,
        'crops': {1: 'apple', 2: 'organe'}
    } 
    ]

    y = FlaskWebProject1.SampleDTO.SampleDTO
    serialized= json.dumps(y, sort_keys=True, indent=3)
    #for val in x._cropSummary:
    #    tasks.extend(val)
    complex = dict(a=FlaskWebProject1.SampleDTO.SampleDTO(), when=datetime(2016, 3, 7))   
    return jsonify({'farms': complex})
    #return jsonify({'farms': serialized})

@app.route('/todo/api/v1.0/getRecord', methods=['GET'])
def get_sample():
    farmDetail = FarmDetail() 
    resultRecord = farmDetail.getRecord('f1')
    #jsonResult = "{""""farmdetails"""":{"
    #jsonResult = """farmcode"""
    dblQot ="\""
    #jsonResult = " \"farmcode\":\""+ resultRecord.farmCode+ "\""  
    jsonResult = "{"
    jsonResult += dblQot + "farmcode" + dblQot + ":" + dblQot+ resultRecord.farmCode+ dblQot 
    jsonResult += ", "
    jsonResult += dblQot + "farmName" + dblQot + ":" + dblQot+ resultRecord.farmName+ dblQot 
   
    jsonResult += ","
    jsonResult += dblQot + "cropDetail" + dblQot  + ":" +  "["
    listQuery = ""
    for record in resultRecord.cropMaster:
        if listQuery != "" :
            listQuery += ", "

        listQuery += "{" 
        listQuery +=  dblQot + "cropCode" + dblQot + ":" + dblQot+ record.code + dblQot 
        listQuery += ", "
        listQuery +=  dblQot + "cropName" + dblQot + ":" + dblQot+ record.cropName+ dblQot       
        listQuery += "}" 

    jsonResult += listQuery + "]"
    
    jsonResult += "}"
    
    return jsonResult
    #simple = dict(cropsList=resultRecord.cropMaster, 
    #          farmcode=resultRecord.farmCode,
    #          farmname=resultRecord.farmName)
    #simple = dict(cropsList=resultRecord.cropMaster, 
    #          farmcode=resultRecord.farmCode,
    #          farmname=resultRecord.farmName)
    
    #print(json.dumps(resultRecord.cropMaster))
    #return jsonify({'farms': simple})
    #return jsonify({'farms': simple})

@app.route('/todo/api/v1.0/testme', methods=['GET'])
def get_testme():    

    contacts = {"xxx-xxx-xxxx": "Joe",
                "yyy-yyy-yyyy": "Joe",
                "zzz-zzz-zzzz": "Ane",
                "aaa-aaa-aaaa": "Rod",
            }

    apps     = ["facebook",
                "linkedin",
                "twitter"] 

    myMobile        = MobilePhone(contacts, apps)
    jsonString      = MobilePhoneEncoder().encode(myMobile)
    print(myMobile)
    return myMobile