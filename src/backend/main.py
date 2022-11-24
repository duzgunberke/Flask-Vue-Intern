import mongoengine as db
from api_constant import mongo_password
database_name = "interntask"
password =mongo_password

from classes import User,Blog 

from flask import Flask, jsonify, request
from pymongo import MongoClient
from flask_cors import CORS 
from bson import ObjectId
import json
import jwt
from datetime import datetime, timedelta
from flask_bcrypt import Bcrypt
from functools import wraps


user=User(name="Beyza",surname="Sonkaya",username="beyzos",password="123456",email="beyzz@gmail.com")
user.save()

 #region Sonra ise yarar
 
# print("\nFetch a blog")
# blog=Blog.objects(blog_id=1).first()
# # print(blog.to_json())
# print("\nUpdate a blog")
# blog.update(name="Deneme 2",
#             author="Efe")
# print(blog.to_json())


# print("\n Fetch all blogs")
# blogs=[]
# for blog in Blog.objects():
#     blogs.append(blog.to_json())
# print(blogs)    

# print("\n Find blog whose name contains Selam")
# for blog in Blog.objects(name__contains="Selam"):
#     blogs.append(blog.to_json())


# print("\nDelete a blog")
# blog =Blog.objects(blog_id=2).first()
# blog.delete()

#endregion

app= Flask(__name__)
CORS(app, resources={r"/*":{'origins':"*"}})
bcrypt = Bcrypt(app)
secret = "***************"
app.config.from_object(__name__)

DB_URL="mongodb+srv://duzgunberke:10.s0Bi0@pythoncluster.g4lwsqz.mongodb.net/{}?retryWrites=true&w=majority".format(database_name)
db.connect(host=DB_URL)

def tokenReq(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "Authorization" in request.headers:
            token = request.headers["Authorization"]
            try:
                jwt.decode(token, secret)
            except:
                return jsonify({"status": "fail", "message": "unauthorized"}), 401
            return f(*args, **kwargs)
        else:
            return jsonify({"status": "fail", "message": "unauthorized"}), 401
    return decorated


@app.route('/',methods=['GET'])
def greetings():
     return("Hi everyone, this project is working !!!")


# @app.route('/shark',methods=['GET'])
# def shark():
#     return("This is a Sharkkkk")

# if __name__ == '__main__':
#     app.run(debug=True)