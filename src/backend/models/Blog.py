from mongoengine import *
import mongoengine as db
import json
from bson import json_util

class Blog(Document):
    title = StringField(Required=True)
    author = StringField(Required=True)
    description = StringField(Required=True)
    
    def to_json(self):
        return {
            "_id": str(self.pk),
            "title": self.title,
            "author": self.author,
            "description": self.description
        } 
  