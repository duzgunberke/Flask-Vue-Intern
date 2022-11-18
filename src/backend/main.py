

import mongoengine as db
from api_constant import mongo_password
database_name = "interntask"
password =mongo_password
DB_URL="mongodb+srv://duzgunberke:10.s0Bi0@pythoncluster.g4lwsqz.mongodb.net/{}?retryWrites=true&w=majority".format(database_name)
db.connect(host=DB_URL)


class Blog(db.Document):
    blog_id=db.IntField()
    name=db.StringField()
    author=db.StringField()
    
    def to_json(self):
        return{
            "blog_id": self.blog_id,
            "name": self.name,
            "author": self.author
        }

print("\n Create a blog")
blog=Blog(blog_id=1,
          name="Deneme",
          author="Berke"
        )
blog.save()


print("\nFetch a blog")
blog=Blog.objects(blog_id=1).first()
# print(blog.to_json())
print("\nUpdate a blog")
blog.update(name="Deneme 2",
            author="Efe")
print(blog.to_json())

print("\n Create a another blog")
blog=Blog(blog_id=2,
          name="Deneme 3",
          author="Aslı"
        )
blog.save()

print("\n Create a another blog")
blog=Blog(blog_id=3,
          name="Selam Deneme",
          author="Aslı"
        )
blog.save()

print("\n Fetch all blogs")
blogs=[]
for blog in Blog.objects():
    blogs.append(blog.to_json())
print(blogs)    

print("\n Find blog whose name contains Selam")
for blog in Blog.objects(name__contains="Selam"):
    blogs.append(blog.to_json())


print("\nDelete a blog")
blog =Blog.objects(blog_id=2).first()
blog.delete()

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