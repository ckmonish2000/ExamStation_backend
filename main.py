# imports
from flask import Flask,jsonify,request,make_response
from werkzeug.routing import Rule
import json
import jwt
from mongoengine import connect


from views.Create_Login_Student import createSingleStudent
from views.Create_Login_Student import StudentLogin
import views.Create_Login_Teacher as TeacherLogin
import views.Get_Post_Seating as Seating

# initializations

app=Flask(__name__)
app.config["SECRET_KEY"]="NEwTest123"
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
    
    




if __name__=="__main__":
    app.run(debug=True)
