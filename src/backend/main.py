import mongoengine as db
from api_constant import mongo_password
database_name = "interntask"
password = mongo_password

from classes import User,Blog 
from flask import Flask, jsonify,request, Response, make_response
from flask_cors import CORS 
from bson import ObjectId
import json
import jwt
from datetime import datetime, timedelta
from flask_bcrypt import Bcrypt
from functools import wraps
from pymongo import MongoClient
from flasgger import Swagger


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

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
swagger = Swagger(app)
bcrypt = Bcrypt(app)
app.config["SECRET_KEY"] = "csharpbetternthanpython18"
DB_URL="mongodb+srv://duzgunberke:10.s0Bi0@pythoncluster.g4lwsqz.mongodb.net/{}?retryWrites=true&w=majority".format(database_name)
db.connect(host=DB_URL)

print("\n Fetch all blogs")
blogs=[]
for blog in Blog.objects():
    blogs.append(blog.to_json())
print(blogs) 


def tokenReq(f):
    @wraps(f)
    def decorated(*args, **kwargs):
         token = None

         if 'token' in request.headers:
            token = request.headers['token']

         if not token:
            return jsonify({'message': 'a valid token is missing'}),401
         try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=[
                'HS256'])  
            current_user = User.objects.get(username=data["username"])

         except:
             return ('', 204)

         return f(current_user, *args, **kwargs)
     
    return decorated

#region Default path
@app.route('/',methods=['GET'])
def greetings():
     return"Hi everyone, this project is working !!!",200
#endregion

#region Get All And Insert One Blog
@app.route('/blogs', methods=['GET', 'POST'])
def index():
    res = []
    code = 500
    status = "fail"
    message = ""
    try:
        if (request.method == 'POST'):
            res = db['interntask.blog'].insert_one(request.get_json())
            if res.acknowledged:
                message = "item saved"
                status = 'successful'
                code = 201
                res = {"_id": f"{res.inserted_id}"}
            else:
                message = "insert error"
                res = 'fail'
                code = 500
        else:
             blogs=[]
             for blog in Blog.objects():
                 blogs.append(blog.to_json())   
             if res:
                 message = "blogs retrieved"
                 status = 'successful'
                 code = 200
             else:
                 message = "no blogs found"
                 status = 'successful'
                 code = 200
    except Exception as ee:
        res = {"error": str(ee)}
    return jsonify({"status":status,'data': res, "message":message}), code
#endregion

#region Get One and update one
@app.route('/getblog/<item_id>', methods=['GET', 'POST'])
@tokenReq
def by_id(item_id):
    data = {}
    code = 500
    message = ""
    status = "fail"
    try:
        if (request.method == 'POST'):
            res = db['interntask.blog'].update_one({"_id": ObjectId(item_id)}, { "$set": request.get_json()})
            if res:
                message = "updated successfully"
                status = "successful"
                code = 201
            else:
                message = "update failed"
                status = "fail"
                code = 404
        else:
            data =  db['interntask.blog'].find_one({"_id": ObjectId(item_id)})
            data['_id'] = str(data['_id'])
            if data:
                message = "item found"
                status = "successful"
                code = 200
            else:
                message = "update failed"
                status = "fail"
                code = 404
    except Exception as ee:
        message =  str(ee)
        status = "Error"

    return jsonify({"status": status, "message":message,'data': data}), code
#endregion


#region Signup
@app.route('/signup', methods=['POST'])
def save_user():
    if request.method == "POST":
        name = request.json['name']
        surname = request.json['surname']
        username = request.json['username']
        password = request.json['password']
        email = request.json['email']

        password = bcrypt.generate_password_hash(password).decode('utf-8')

        if username and password and email:                
            user = User(name=name, surname=surname,
                     username=username, password=password, email=email)
            user.save()  

    return {'message': 'successful user adding'}

        
#endregion

#region Login
@app.route('/login', methods=['POST'])
def login():
    if request.method == "POST":
        username = request.json['username']
        password = request.json['password']  # password
        user = User.objects.get(username=username)

        if bcrypt.check_password_hash(user.password, user["password"]):
                token = jwt.encode({'username': username, 'exp': datetime.datetime.utcnow(
                ) + datetime.timedelta(minutes=15)}, app.config['SECRET_KEY'])
                return jsonify({'token': token})

        else:
                return {"message": "Password invalid"}

#endregion            







# @app.route('/shark',methods=['GET'])
# def shark():
#     return("This is a Sharkkkk")

if __name__ == '__main__':
    app.run(use_reloader=True,debug=True, host="0.0.0.0", port=5000)