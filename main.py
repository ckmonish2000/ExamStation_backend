# imports
from flask import Flask,jsonify,request,make_response
from werkzeug.routing import Rule
import json
import jwt
from mongoengine import connect
from flask_cors import CORS

from controller.Create_Login_Student import createSingleStudent
from controller.Create_Login_Student import StudentLogin
import controller.Create_Login_Teacher as TeacherLogin
import controller.Get_Post_Seating as Seating
from controller.Contact import Contact
# initializations

app=Flask(__name__)
app.config["SECRET_KEY"]="NEwTest123"
CORS(app)
con=connect("newdb")



# create a newstudent
app.add_url_rule("/NewStudent",view_func=createSingleStudent,methods=["POST"])

# login as student
app.add_url_rule("/studentLogin",view_func=StudentLogin,methods=["POST"])


# create new teacher
app.add_url_rule("/NewTeacher",view_func=TeacherLogin.createSingleTeacher,methods=["POST"])


# login as Teacher
app.add_url_rule("/teacherLogin",view_func=TeacherLogin.TeacherLogin,methods=["POST"])  

# new seating upload
app.add_url_rule("/newSeating",view_func=Seating.NewSeating,methods=["POST"])

# get all seating
app.add_url_rule("/getAllSeating",view_func=Seating.getAllSeating)

# get specific seating

app.add_url_rule("/getStudentSeating",view_func=Seating.getSpecificSeat,methods=["GET"])


app.add_url_rule("/deleteSeat",view_func=Seating.DeleteSeating,methods=["POST"])
 
app.add_url_rule("/contactus",view_func=Contact)
    
if __name__=="__main__":
    app.run(port=80,debug=True)
