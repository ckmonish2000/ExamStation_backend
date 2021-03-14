import sys
sys.path.append("..")
from flask import jsonify,request,make_response
from mongoengine import *
from backend.model.SeatingArragements import Seating
import json
from backend.utils.token_check import CheckIFLogedin
    



@CheckIFLogedin
def NewSeating():
    if(request.method=="POST"):
        StudentName=request.get_json()["StudentName"]
        RollNo=request.get_json()["RollNo"]
        classRoom=request.get_json()["classRoom"]
        floor=request.get_json()["floor"]
        try:
            seat=Seating(StudentName=StudentName,RollNo=RollNo,classRoom=classRoom,floor=floor)
            seat.save()
            return jsonify({"Seating_created":True,"Student":seat.StudentName})
        except:
            return "something went wrong"

@CheckIFLogedin
def getAllSeating():
    seat=Seating.objects
    json_data=seat.to_json()
    return jsonify( json.loads(json_data))


@CheckIFLogedin
def getSpecificSeat():
    rollno=request.get_json()["RollNo"]
    Seat=Seating.objects(RollNo=rollno)
    return jsonify(json.loads(Seat.to_json()))

@CheckIFLogedin
def DeleteSeating():
    seat=Seating.objects(RollNo="18sje923")
    json_data=seat.to_json()
    seat.delete()
    return jsonify( json.loads(json_data))
