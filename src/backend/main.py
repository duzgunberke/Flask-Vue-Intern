import mongoengine as db

database_name = "interntask"

from models.User import User
from models.Blog import Blog
from models.User import UserRoles 

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
            current_user = User.objects(username=data.get('username')).first()                 
        except:
            return make_response(jsonify({"message": "Invalid token!"}), 401)
         # Return the user information attached to the token
        return f(current_user,*args, **kwargs)                                                        
    return decorator
#endregion

#region Default path
@app.route('/',methods=['GET'])
def greetings():
     return jsonify({"message": "Hi everyone, this project is working 🚀🚀🚀"}),200
#endregion

#region Get All Blogs
@app.route('/blogs',methods=['GET'])
def all_blogs():
    """
    A method that retrieves the blog with the id 
    value sent when the get method is used, and updates
    the blog with the sent id value when the put method is used.

    Parameters
    ----------
    current_user: objects
        Containing the information of the currently logged in user objects
    id: str
        id value kept as primary key for blogs in mongodb
    
    Returns
    -------
    res: blog array
        An array containing all blogs in db
    message & status: string
        message and status informing whether the operation was successful or not
    code: int
       It throws a 404 error when the blog objects cannot be found in db.
       Returns 200 status code if the operation was done successfully   
       It throws a 504 error when the http method the user is using is incorrect

    Raises
    ------
    Exception
        It throws a 404 error when the blog objects cannot be found in db.
        It throws a 504 error when the http method the user is using is incorrect

    """
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
             code = 404
        else:
            message = "This method is not correct !"  
            status = 'failed'
            code = 504
            return jsonify({"status":status,"message": message}),code  
    except Exception as ee:
        res = {"error": str(ee)}
    return jsonify({"status":status,'data': res, "message":message}), code    
#endregion

#region Get Blog By ID               
@app.route('/blogbyid', methods=["POST"])
def blog_by_id():
    """
    A method designed to enter the details page
    of the blog. It brings us the matching object
    in the blog collection in the database according 
    to the id value sent.

    Parameters
    ----------
    id: str
        id value kept as primary key for blogs in mongodb
    
    Returns
    -------
    blog: object
        The object of the blog with the submitted id
       
    """
    if request.method == "POST":
        id = request.json['id']
        blog = Blog.objects.get(id=id)
        return make_response(jsonify(blog.to_json()))
#endregion

#region Get Blog By Author
@app.route('/blogbyauthor', methods=["GET"])
@token_Req
def blog_by_author(current_user):
    """
    The method that lists all the blogs that
    the logged in user has written and brings
    them to her so that he/she can perform crud operations on them.

    Parameters
    ----------
    current_user: objects
        Containing the information of the currently logged in user objects
    
    Returns
    -------
    res: blog array
        An array containing all blogs from the desired author
    message & status: string
        Message and status informing whether the operation was successful or not
    code: int
       It throws a 504 error when the http method the user is using is incorrect
       Returns 200 status code if the operation was done successfully   
    Raises
    ------
    Exception
       It throws a 504 error when the http method the user is using is incorrect

    """
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
            message = "This method is not correct !" 
            status = "fail"
            code = 504
            return jsonify({"status" : status,"message": message}),code    
    except Exception as ee:
        res = {"error": str(ee)}
    return jsonify({"status":status,'data': res, "message":message}), code    
#endregion

#region Get Blogs By Author On Mainpage
@app.route('/authorblogs/<author>', methods=["GET"])
def blogs_by_buthor(author):
    """
    A method that allows us to view other
    blogs written by that author when we enter
    the details of the blog and click on its author.

    Parameters
    ----------
    author: string
        Username of the author sent in http url
    
    Returns
    -------
    res: blog array
        An array containing all blogs from the desired author
    message & status: string
        Message and status informing whether the operation was successful or not
    code: int
       It throws a 504 error when the http method the user is using is incorrect
       Returns 200 status code if the operation was done successfully     
       
    Raises
    ------
    Exception
       It throws a 504 error when the http method the user is using is incorrect

    """
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
            message = "This method is not correct !" 
            status = "fail"
            code = 504
            return jsonify({"status": status, "message": message}),code    
    except Exception as ee:
        res = {"error": str(ee)}
    return jsonify({"status":status,'data': res, "message":message}), code    
#endregion

#region Insert One Blog
@app.route('/addblog', methods=['POST'])
@token_Req
def add_blog(current_user):
    """
    The username of the logged in user is assigned
    as the blogger. A method written to add to 
    the database after the description and title are entered

    Parameters
    ----------
    current_user: objects
        Containing the information of the currently logged in user objects
        
    Returns
    -------
    message & status: string
        message and status informing whether the operation was successful or not
    res: blog objects field
        added blog title    
    code: int
       It throws a 500 error when due to not filling all required folds
       If she tries to login to an unauthorized endpoint, she gets a 403 error.
       
    Raises
    ------
    Exception
       If the user trying to run the method 
       does not have admin or author privileges, it cannot access.

    """
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
                message = "This user role is not correct !!!" 
                status = "fail"
                code = 403
                return jsonify({"status": status, "message":message}),code   
        else:
            message = "This method is not correct !"
            status = "fail"
            code = 504
            return jsonify({"status": status, "message":message}),code
    except Exception as ee:
        res = {"error": str(ee)}
    return jsonify({"status":status,'data': res, "message":message}), code
#endregion

#region Update and Get One Blog          
@app.route('/blog/<id>', methods=['GET', 'PUT'])
@token_Req 
def edit_blog_by_id(current_user,id):
    """
    A method that retrieves the blog with the id 
    value sent when the get method is used, and updates
    the blog with the sent id value when the put method is used.

    Parameters
    ----------
    current_user: objects
        Containing the information of the currently logged in user objects
    id: str
        id value kept as primary key for blogs in mongodb
    
    Returns
    -------
    message & status: string
        message and status informing whether the operation was successful or not
    code: int
       It throws a 404 error when the blog object suitable for the sent id cannot be found.
       If she tries to login to an unauthorized endpoint, she gets a 403 error.
       
    Yields
    ------
    data: blog objects 
        Contains the information of the blog taken 
        according to the id sent with the get value

    Raises
    ------
    Exception
        It throws a 404 error when the blog object suitable for the sent id cannot be found.
        If she tries to login to an unauthorized endpoint, she gets a 403 error.

    """
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
                message = "This user role is not correct!"
                status = "fail"
                code = 403
                return jsonify({"status": status, "message": message}),code     
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
    """
    The method that deletes that blog according to the blog id value sent

    Parameters
    ----------
    current_user: objects
        Containing the information of the currently logged in user objects
    _id: str
        id value kept as primary key for blogs in mongodb
    
    Returns
    -------
    message & status string
        message and status informing whether the operation was successful or not
    code:int
       It throws a 404 error when the blog object suitable for the sent id cannot be found.
       
    Yields
    ------
    data: blog objects 
        Contains the information of the blog taken 
        according to the id sent with the get value

    Raises
    ------
    Exception
        It throws a 404 error when the blog object suitable for the sent id cannot be found.
    """
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
    """
    A method that allows us to save the user's information to create an account

    Parameters
    ----------
    null
    
    Returns
    -------
    message & status: string
        message and status informing whether the operation was successful or not

    Raises
    ------
    Exception
       In case of sending missing field, it throws an error message

    """
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
            return jsonify({'message': 'Fill in the required fields'})   

    return jsonify({'message': 'successful user adding'})

        
#endregion

#region Login
@app.route('/login', methods=['POST'])
def login():
    """
    A method by which registered users can log in
    if successful as a result of comparison with their 
    passwords in the database. At the same time, we create
    a special token value for the logged in user.

    Parameters
    ----------
    null
    
    Returns
    -------
    message: string
        message and status informing whether the operation was successful or not
    token: string
        a custom-built JWT for each logged-in user
    user: user objects
        User objects
       
    Yields
    ------
    data: blog objects 
        Contains the information of the blog taken 
        according to the id sent with the get value

    Raises
    ------
    Exception
        According to the information given, the user could not be found in the database, it throws a 401 error

    """
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
        return jsonify({"message": "Password invalid"})

#endregion            

#region Logout
@app.route('/logout', methods=['POST'])

def logout():
    return jsonify({"message": True})
#endregion

#region Edit Users
@app.route('/edituser', methods=["PUT"])
@token_Req
def edit_users(current_user):
    """
    The method to be used when the logged in user wants to update his/her information

    Parameters
    ----------
    current_user: objects
        Containing the information of the currently logged in user objects
    
    Returns
    -------
    message & status: string
        message and status informing whether the operation was successful or not
    code: int
       It throws a 404 error when the blog object suitable for the sent id cannot be found.
       If he/she tries to login to an unauthorized endpoint, gets a 403 error.
       It throws a 504 error when the http method the user is using is incorrect
       
    Yields
    ------
    data: blog objects 
        Contains the information of the blog taken 
        according to the id sent with the get value

    Raises
    ------
    Exception
        It throws a 404 error when the user object suitable for the sent id cannot be found.
        If he/she tries to login to an unauthorized endpoint, she gets a 403 error.

    """
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
                status = "fail"
                code = 403
                message = "This user role is not correct!"
                return jsonify({"status": status, "message": message}),code       
        else:
            status = "fail"
            code = 504
            message = "This method is not correct"
            return jsonify({"status" : status,"message" : message }),code
    except Exception as ee:
        message =  str(ee)
        status = "Error"

    return jsonify({"status": status, "message":message}), code
    
#endregion

#region Get Users
@app.route('/users', methods=["GET"])
@token_Req
def users(current_user):
    """
    With this method, we pull the entire collection of users in the database.

    Parameters
    ----------
    current_user: objects
        Containing the information of the currently logged in user objects
    
    Returns
    -------
    message: string
        Message and status informing whether the operation was successful or not
    users: object
        It pulls all the values in the User collection without filtering.
       
    Raises
    ------
    Exception
        If the user trying to run the method 
        does not have admin privileges, it cannot access.

    """
    if current_user["role"]=='admin':
        users = []
        for user in User.objects():  
            users.append(user.to_json())
            print(users)
        return make_response(jsonify(users))
    else:
        return jsonify({'message': 'User is not a admin !'}) 
#endregion

#region Get Current User
@app.route('/currentuser', methods=['GET'])
@token_Req
def current_user_in_token(current_user):
    """
    After the user logs in, all the information of 
    the logged in user is retrieved thanks
    to the username information stored in the
    token created after logging in for the user value that
    we will keep as the state on the front.

    Parameters
    ----------
    current_user: objects
        Containing the information of the currently logged in user objects
 
    Returns
    -------
    user: objects
        login user information   
    """
    username=current_user['username']
    user=User.objects.get(username=username)
    return make_response(jsonify(user.to_json()))
#endregion

if __name__ == '__main__':
    
    app.run(use_reloader=True,debug=True, host="0.0.0.0", port=5000)