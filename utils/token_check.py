from flask import make_response,request
import jwt

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