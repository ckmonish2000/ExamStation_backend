from mongoengine import *

class ContactUs(Document):
    number=IntField()
    email=EmailField()
