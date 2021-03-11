from mongoengine import *

class CreateStudent(Document):
    RollNo=StringField(required=True,unique=True)
    password=StringField(required=True)
    name=StringField(required=True)


