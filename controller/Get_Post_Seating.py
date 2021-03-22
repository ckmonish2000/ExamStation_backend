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
        exam=request.get_json()["exam"]
        try:
            seat=Seating(StudentName=StudentName,RollNo=RollNo,classRoom=classRoom,floor=floor,exam=exam)
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
    rollno=request.args.get("RollNo")
    Exam=request.args.get("exam")
    seat=Seating.objects(exam=Exam,RollNo=rollno)
    # for i in seat:
    #     print(i.to_json())
    # return jsonify(json.loads(Seat.to_json()))
    
    return jsonify({"data":seat.to_json()})

@CheckIFLogedin
def DeleteSeating():
    roll=request.get_json()["RollNo"]
    seat=Seating.objects(RollNo=roll)
    json_data=seat.to_json()
    seat.delete()
    return jsonify( json.loads(json_data))
