import sys
sys.path.append("..")
from flask import request
from backend.model.contactUs import ContactUs


def Contact():
    number=request.args.get('number')
    email=var=request.args.get('email')
    try:
        x=ContactUs(number=number, email=email)
        x.save()
        return {"created":True}
    except:
        return {"created":False}
