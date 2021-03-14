import sys
sys.path.append("..")
from flask import jsonify,request
from mongoengine import *
from backend.model.SeatingArragements import Seating

    

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
        except(e):
            return e