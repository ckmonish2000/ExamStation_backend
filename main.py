# imports
from flask import Flask,jsonify,request,make_response
from mongoengine import *
import json
from model.SeatingArragements import Seating
from model.StudentLogin import CreateStudent
import jwt


# initializations
app=Flask(__name__)
app.config["SECRET_KEY"]="NEwTest123"
con=connect("newdb")


def CheckIFLogedin(func):
    def inner(*args,**kwargs):
        token=request.args.get("token")
        if not token:
            return make_response("no token",404)
        
        try:
            data=jwt.decode(token,app.config["SECRET_KEY"],algorithms="HS256")
            return func(*args,**kwargs)
        except:
            return  "Invalid"
        
    return inner
    
    



@app.route("/test")
@CheckIFLogedin
def index():
    return "welcome to protected"

# create a newstudent
@app.route("/NewStudent")
def createSingle():
    Rollno=request.get_json()["roll"]
    password=request.get_json()["pass"]
    sname=request.get_json()["name"]
    try:
        student=CreateStudent(RollNo=Rollno,password=password,name=sname)
        student.save()
    # token=jwt.encode({"user":"mk","password":"123"},app.config["SECRET_KEY"])
        return jsonify({"Created":True,"roll":student.RollNo})
    except:
        return jsonify({"Created":False,"message":"something went wrong try entering a unique rollno"})


for i in CreateStudent.objects():
            print(i)

# login as student
@app.route("/studentLogin")
def studentLogin():
    username=request.get_json()["username"]
    password=request.get_json()["password"]
    try:
        i=CreateStudent.objects(RollNo=username)[0]
        val={"RollNo":i.RollNo,"name":i.name,"password":i.password}    
        if password==val["password"] and username== val["RollNo"]:
            token=jwt.encode({"RollNo":username,"password":password},app.config["SECRET_KEY"])
            return jsonify({"loggedin":True,"token":token})
    
    except: return jsonify({"loggedin":False,"token":"Invalid Token"})
            








if __name__=="__main__":
    app.run(debug=True)
