import mongoengine as db

database_name = "interntask"

from models.User import User
from models.Blog import Blog

from flask import Flask, jsonify,request, Response, make_response
from flask_cors import CORS 
from bson import ObjectId
import json
import jwt
import datetime
from flask_bcrypt import Bcrypt
from functools import wraps
from pymongo import MongoClient


app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
bcrypt = Bcrypt(app)

#region Conf
app.config["SECRET_KEY"] = "csharpbetternthanpython18"
DB_URL="mongodb+srv://duzgunberke:10.s0Bi0@pythoncluster.g4lwsqz.mongodb.net/{}?retryWrites=true&w=majority".format(database_name)
db.connect(host=DB_URL)
#endregion

#region JWT Token
def token_Req(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        # ensure the jwt-token is passed with the headers
        if 'Authorization' in request.headers or 'x-access-token' in request.headers or 'token' in request.json:
            token = request.headers.get(
                'x-access-token', None) or request.headers.get('Authorization')
            token = token.replace('Bearer ', '')
        if not token: # throw error if no token provided
            return make_response(jsonify({"message": "A valid token is missing!"}), 401)
        try:
           # decode the token to obtain user email
            data = jwt.decode(token, app.config['SECRET_KEY'],algorithms=['HS256'])
            current_user = User.objects(username=data.get('username')).first()                    #Burada hata var !!!!
        except:
            return make_response(jsonify({"message": "Invalid token!"}), 401)
         # Return the user information attached to the token
        return f(current_user,*args, **kwargs)                                                           #current user donunce hata atıyor
    return decorator
#endregion

#region Default path
@app.route('/',methods=['GET'])
def greetings():
     return"Hi everyone, this project is working 🚀🚀🚀",200
#endregion

#region Get All Blogs
@app.route('/blogs',methods=['GET'])
def allBlogs():
    res = []
    code = 500
    status = "fail"
    message = ""
    try:
        if(request.method == 'GET'):
            for blog in Blog.objects():  
             res.append(blog.to_json())
                 
            if res:
             message = "blogs retrieved"
             status = 'successful'
             code = 200
            else:
             message = "no blogs found"
             status = 'successful'
             code = 200
        else:
            return "This method is not correct !"     
    except Exception as ee:
        res = {"error": str(ee)}
    return jsonify({"status":status,'data': res, "message":message}), code    
#endregion

#region Get Blog By ID               
@app.route('/getblogbyid', methods=["POST"])
def blogById():
    if request.method == "POST":
        id = request.json['id']
        blog = Blog.objects.get(id=id)
        return make_response(jsonify(blog.to_json()))
#endregion

#region Get Blog By Author
@app.route('/getblogbyauthor', methods=["GET"])
@token_Req
def blogbybuthor(current_user):
    res = []
    code = 500
    status = "fail"
    message = ""
    try:
        if(request.method == 'GET'):
            for blog in Blog.objects(author=current_user["username"]):  
             res.append(blog.to_json())
            if res:
             message = "blogs retrieved"
             status = 'successful'
             code = 200
            else:
             message = "no blogs found"
             status = 'successful'
             code = 200
        else:
            return "This method is not correct !"     
    except Exception as ee:
        res = {"error": str(ee)}
    return jsonify({"status":status,'data': res, "message":message}), code    
#endregion

#region Get Blogs By Author On Mainpage
@app.route('/authorblogs/<author>', methods=["GET"])
def blogsbybuthor(author):
    res = []
    code = 500
    status = "fail"
    message = ""
    try:
        if(request.method == 'GET'):
            for blog in Blog.objects(author=author):  
             res.append(blog.to_json())
            if res:
             message = "blogs retrieved"
             status = 'successful'
             code = 200
            else:
             message = "no blogs found"
             status = 'successful'
             code = 200
        else:
            return "This method is not correct !"     
    except Exception as ee:
        res = {"error": str(ee)}
    return jsonify({"status":status,'data': res, "message":message}), code    
#endregion

#region Insert One Blog
@app.route('/addblog', methods=['POST'])
@token_Req
def addblog(current_user):
    res = []
    code = 500
    status = "fail"
    message = ""
    try:
        if (request.method == 'POST'):
            if(current_user["role"]=="author" or current_user["role"]=="admin"):
                title = request.json['title']
                author = current_user["username"]
                description = request.json['description']
                blog=Blog(title=title, author=author,description=description)
                blog.save()
                
                if  blog !=0:
                    message = "item saved"
                    status = 'successful'
                    code = 201
                    res = "{}".format(blog.title)
                else:
                    message = "insert error"
                    status="fail"
                    res = 'Not working'
                    code = 500
            else:
                return "This user role is not correct !!!"        
        else:
             return "This method is not correct !"
    except Exception as ee:
        res = {"error": str(ee)}
    return jsonify({"status":status,'data': res, "message":message}), code
#endregion

#region Update and Get One Blog           
@app.route('/blog/<id>', methods=['GET', 'PUT'])
@token_Req 
def by_id(current_user,id):
    data = {}
    code = 500
    message = ""
    status = "fail"
    try:
        if (request.method == 'PUT'):
            if(current_user["role"]=="author" or current_user["role"]=="admin"):
                body=request.get_json()
                blog=Blog.objects(id=id).first()
                blog.update(**body)
                if blog:
                    message = "updated successfully"
                    status = "successful"
                    code = 201
                else:
                    message = "update failed"
                    status = "fail"
                    code = 404
            else:
                return "This user role is not correct!"        
        else:
            data = Blog.objects(id=id).first().to_json()
            if data:
                message = "item found"
                status = "successful"
                code = 200
            else:
                message = "item not found"
                status = "fail"
                code = 404
    except Exception as ee:
        message =  str(ee)
        status = "Error"

    return jsonify({"status": status, "message":message,'data': data}), code
#endregion

#region Delete Blog                     
@app.route('/delete/<_id>', methods=['DELETE'])
@token_Req
def delete_one(current_user,_id):
    data =[]
    code = 500
    message = ""
    status = "fail"
    try:
        if (request.method == 'DELETE'):
            blog=Blog.objects(id=_id).first()
            blog.delete()
            if blog:
                message = "Delete successfully"
                status = "successful"
                code = 201
            else:
                message = "Delete failed"
                status = "fail"
                code = 404
        else:
            message = "Delete Method failed"
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
        else:
            return {'message': 'Fill in the required fields'}   

    return {'message': 'successful user adding'}

        
#endregion

#region Login
@app.route('/login', methods=['POST'])
def login():
    if request.method == "POST":
            auth = request.get_json()
    if not auth or not auth.get('username') or not auth.get('password'):
        return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic-realm= "Login required!"'})

    user = User.objects.get(username=auth['username'])
    
    if not user:
        return make_response('Could not verify user, Please signup!', 401, {'WWW-Authenticate': 'Basic-realm= "No user found!"'})
    if bcrypt.check_password_hash(user["password"], auth.get('password')):
       token = jwt.encode({'username': user.username}, app.config['SECRET_KEY'])
               
       return jsonify({'token': token,"user":user.to_json()})

    else:
        return {"message": "Password invalid"}

#endregion            

#region Logout
@app.route('/logout', methods=['POST'])

def logout():
    return jsonify({"message": True})
#endregion

#region Edit Users
@app.route('/edituser', methods=["PUT"])
@token_Req
def editUsers(current_user):
    data = {}
    code = 500
    message = ""
    status = "fail"
    try:
        if (request.method == 'PUT'):
            if(current_user["role"]=="author" or current_user["role"]=="admin"):
                body=request.get_json()
                user=User.objects(username=current_user["username"])
                print(user)
                user.update(**body)
                if user:
                    message = "updated successfully"
                    status = "successful"
                    code = 201
                else:
                    message = "update failed"
                    status = "fail"
                    code = 404
            else:
                return "This user role is not correct!"        
        else:
             return "This method is not correct"
    except Exception as ee:
        message =  str(ee)
        status = "Error"

    return jsonify({"status": status, "message":message,'data': data}), code
    
#endregion

#region Get Users
@app.route('/users', methods=["GET"])
@token_Req
def users(current_user):
    if current_user["role"]=='admin':
        users = []
        for user in User.objects():  
            users.append(user.to_json())
            print(users)
        return make_response(jsonify(users))
    else:
        return {'message': 'User is not a admin !'} 
#endregion

#region Get Current User
@app.route('/currentuser', methods=['GET'])
@token_Req
def currentuser(current_user):
    username=current_user['username']
    user=User.objects.get(username=username)
    return make_response(jsonify(user.to_json()))
#endregion

if __name__ == '__main__':
    
    app.run(use_reloader=True,debug=True, host="0.0.0.0", port=5000)