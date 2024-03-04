from django.db import models
from django.contrib.auth.models import User
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    registerdate = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} {self.lastname}"
    
class Post(models.Model):
    user = models.ForeignKey(Author,on_delete=models.CASCADE, 
                             related_name='postlar')
   
    content = models.TextField(max_length = 500)
    postdate = models.DateTimeField(auto_now_add=True)

class Reply(models.Model):
    user=models.ForeignKey(Author,on_delete=models.CASCADE,related_name='replies')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content=models.TextField()
    replydate = models.DateTimeField(auto_now_add = True)

class UserPictures(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.CharField(max_length=100, default = "")