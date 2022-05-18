from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog_article(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField() 
    content=models.TextField()
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    online=models.BooleanField()


class Contact_request(models.Model):
    email = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    content=models.TextField(max_length=250)
    date = models.DateField()