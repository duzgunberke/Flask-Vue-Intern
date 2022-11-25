from mongoengine import *
import mongoengine as db
import datetime
import pytz
from pytz import timezone

class User(db.Document):
    name = StringField()
    surname=StringField()
    username = StringField(Required=True,unique=True)
    password = StringField(Required=True)
    email = EmailField()
    
    def to_json(self):
             return{
             "name": self.name,
             "surname": self.surname,
             "username": self.username,
             "password":self.password,
             "email": self.email
         }
    # utc_now = datetime.datetime.utcnow()
    # utc = pytz.timezone('UTC')
    # aware_date = utc.localize(utc_now)
    # turkey = timezone('Europe/Istanbul')
    # date_modified = DateTimeField(default=aware_date.astimezone(turkey))


class Blog(db.Document):
    user_id = ObjectIdField(Required=True)
    title = StringField(Required=True)
    author = StringField(Required=True)
    description = StringField(Required=True)
    
    def to_json(self):
            return{
            "user_id": self.user_id,
            "author": self.author,
            "title": self.title,
            "description": self.description
        }

    
