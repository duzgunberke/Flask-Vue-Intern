from mongoengine import *
import mongoengine as db
import json
from bson import json_util

class Blog(Document):
    user_id = ObjectIdField(Required=True)
    title = StringField(Required=True)
    author = StringField(Required=True)
    description = StringField(Required=True)
    
    def to_json(self):
            bson_data = {'title': self.title, 'author': self.author,'description': self.description}

            json_data_with_backslashes = json_util.dumps(bson_data)
            json_data = json.loads(json_data_with_backslashes)
            return json_data
    