from flask import make_response,request
import jwt
from functools import wraps


def CheckIFLogedin(func):
    @wraps(func)
    def inner(*args,**kwargs):
        token=request.args.get("token")
        if not token:
            return make_response("no token",404)
        
        try:
            data=jwt.decode(token,"NEwTest123",algorithms="HS256")
            return func(*args,**kwargs)
        except:
            return  "Invalid"
        
    return inner