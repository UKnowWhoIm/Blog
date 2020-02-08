from django.db import models

# Create your models here.
class User(models.Model):
    Name = models.CharField(max_length=40)
    Email = models.CharField(max_length=30,primary_key = True)
    Password = models.CharField(max_length=30)
    IsAdmin = models.BooleanField(default=False)
    
class Post(models.Model):
    Title = models.CharField(max_length=40)
    Content = models.TextField()
    Author = models.ForeignKey(User,on_delete=models.CASCADE)
    Date = models.DateTimeField('Date')
    Likes = models.IntegerField(default=0)
    Votes = models.ManyToManyField(User,related_name='Votes')    
