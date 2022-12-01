from mongoengine import *
import mongoengine as db
import datetime
import pytz
from pytz import timezone
import json
from bson import json_util


class User(Document):
    name = StringField()
    surname=StringField()
    username = StringField(Required=True,unique=True)
    password = StringField(Required=True)
    email = EmailField()
    author = BooleanField(default=False)
    utc_now = datetime.datetime.utcnow()
    utc = pytz.timezone('UTC')
    aware_date = utc.localize(utc_now)
    turkey = timezone('Europe/Istanbul')
    date_modified = DateTimeField(default=aware_date.astimezone(turkey))
    
    def to_json(self):
            bson_data = {'name': self.name, 'surname': self.surname,'username': self.username,'password': self.password,'email': self.email}

            json_data_with_backslashes = json_util.dumps(bson_data)
            json_data = json.loads(json_data_with_backslashes)
            return json_data