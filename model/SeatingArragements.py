from mongoengine import  *

class Seating(Document):
    StudentName=StringField(required=True)
    RollNo=StringField(required=True)
    classRoom=StringField(required=True)
    floor=IntField(required=True)


