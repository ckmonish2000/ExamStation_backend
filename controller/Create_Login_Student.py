from flask import request,jsonify
import sys
sys.path.append("..")
from backend.model.StudentLogin import CreateStudent
import jwt 



def createSingleStudent():
    Rollno=request.get_json()["roll"]
    password=request.get_json()["pass"]
    sname=request.get_json()["name"]
    try:
        student=CreateStudent(RollNo=Rollno,password=password,name=sname)
        student.save()
        return jsonify({"Created":True,"roll":student.RollNo})
    except:
        return jsonify({"Created":False,"message":"something went wrong try entering a unique rollno"})


def StudentLogin():
    username=request.get_json()["username"]
    password=request.get_json()["password"]
    try:
        i=CreateStudent.objects(RollNo=username)[0]
        val={"RollNo":i.RollNo,"name":i.name,"password":i.password}    
        if password==val["password"] and username== val["RollNo"]:
            token=jwt.encode({"RollNo":username,"password":password},"NEwTest123")
            return jsonify({"loggedin":True,"token":token})
        else:
            return jsonify({"loggedin":False,"message":"Invalid  password"})

    
    except: return jsonify({"loggedin":False,"message":"invalid Rollno"})
    


