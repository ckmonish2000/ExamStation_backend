# imports
from flask import Flask,jsonify,request,make_response
from mongoengine import *
import json
from model.SeatingArragements import Seating
from model.StudentLogin import CreateStudent
import jwt
from views.Create_Login_Student import createSingleStudent
from views.Create_Login_Student import StudentLogin

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
    
    






# create a newstudent
app.add_url_rule("/NewStudent",view_func=createSingleStudent)

# login as student
app.add_url_rule("/studentLogin",view_func=StudentLogin)









if __name__=="__main__":
    app.run(debug=True)
