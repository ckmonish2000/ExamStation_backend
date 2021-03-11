from mongoengine import *

class CreateTeacher(Document):
    TeacherId=StringField(required=True,unique=True)
    password=StringField(required=True)
    name=StringField(required=True)