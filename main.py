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


@app.route("/New")
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
        return jsonify({"Created":False,"message":"something went wrong"})
    



if __name__=="__main__":
    app.run(debug=True)
