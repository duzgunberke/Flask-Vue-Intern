def mongo_password():
    return "10.s0Bi0"



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
