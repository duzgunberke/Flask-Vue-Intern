

import mongoengine as db
from api_constant import mongo_password
database_name = "interntask"
password =mongo_password
DB_URL="mongodb+srv://duzgunberke:10.s0Bi0@pythoncluster.g4lwsqz.mongodb.net/{}?retryWrites=true&w=majority".format(database_name)
db.connect(host=DB_URL)
from classes import User,Blog 


# class Blog(db.Document):
#     user_id=db.ObjectIdField(required=True)
#     author=db.StringField(required=True)
#     title = db.StringField(Required=True)
#     description = db.StringField(Required=True)
    
#     def to_json(self):
#         return{
#             "user_id": self.user_id,
#             "author": self.author,
#             "title": self.title,
#             "description": self.description
#         }

# print("\n Create a blog")
# blog=Blog(
#           user_id="637a99320a792735f42e026e",
#           author="Berke",
#           title="Deneme",
#           description="Lorem ipis rem ipis rem "
#         )
# blog.save()

user=User(name="Efe",surname="Dzgn",username="dzgnefe",password="123456",email="duzgunberke2@gmail.com")
user.save()

# print("\nFetch a blog")
# blog=Blog.objects(blog_id=1).first()
# # print(blog.to_json())
# print("\nUpdate a blog")
# blog.update(name="Deneme 2",
#             author="Efe")
# print(blog.to_json())

# print("\n Create a another blog")
# blog=Blog(blog_id=2,
#           name="Deneme 3",
#           author="Aslı"
#         )
# blog.save()

# print("\n Create a another blog")
# blog=Blog(blog_id=3,
#           name="Selam Deneme",
#           author="Aslı"
#         )
# blog.save()

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

# class User(db.Document):
#     name = db.StringField()
#     surname=db.StringField()
#     username = db.StringField(Required=True,unique=True)
#     password = db.StringField(Required=True)
#     email = db.EmailField()
    
#     def to_json(self):
#         return{
#             "name": self.name,
#             "surname": self.surname,
#             "username": self.username,
#             "password":self.password,
#             "email": self.email
#         }

# user=User(
#           name="Berke",
#           surname="Duzgun",
#           username="duzgunberke",
#           password="123456",
#           email="duzgunberke@gmail.com")
# user.save()

# app= Flask(__name__)

# app.config.from_object(__name__)

# CORS(app, resources={r"/*":{'origins':"*"}})


# @app.route('/',methods=['GET'])
# def greetings():
#     return("Hi everyone")


# @app.route('/shark',methods=['GET'])
# def shark():
#     return("This is a Sharkkkk")

# if __name__ == '__main__':
#     app.run(debug=True)