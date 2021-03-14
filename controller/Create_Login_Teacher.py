from flask import request,jsonify
import sys
sys.path.append("..")
from backend.model.TeacherLogin import CreateTeacher
import jwt 



def createSingleTeacher():
    TeacherId=request.get_json()["roll"]
    password=request.get_json()["pass"]
    sname=request.get_json()["name"]
    try:
        Teacher=CreateTeacher(TeacherId=TeacherId,password=password,name=sname)
        Teacher.save()
        return jsonify({"Created":True,"roll":Teacher.TeacherId})
    except:
        return jsonify({"Created":False,"message":"something went wrong try entering a unique TeacherId"})


def TeacherLogin():
    username=request.get_json()["username"]
    password=request.get_json()["password"]
    try:
        i=CreateTeacher.objects(TeacherId=username)[0]
        val={"TeacherId":i.TeacherId,"name":i.name,"password":i.password}    
        if password==val["password"] and username== val["TeacherId"]:
            token=jwt.encode({"TeacherId":username,"password":password},"NEwTest123")
            return jsonify({"loggedin":True,"token":token})
        else:
            return jsonify({"loggedin":False,"message":"Invalid  password"})

    
    except: return jsonify({"loggedin":False,"message":"invalid TeacherId"})
    


