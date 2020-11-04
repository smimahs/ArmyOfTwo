from django.db import models
from django.urls import reverse


# Create your models here.
class Clients(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    password=models.CharField(max_length=20)
    cpassword=models.CharField(max_length=20)
    is_active=models.BooleanField(default=False)

    def __str__(self):
        return self.name
'''
class Employee(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=150)
    companyName=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    mobile=models.CharField(max_length=11)
    password=models.CharField(max_length=20)
    cpassword=models.CharField(max_length=20)
    is_active=models.BooleanField(default=False)

    def __str__(self):
        return self.companyName

'''
class Post(models.Model):

    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=200,unique=True)
    summery=models.CharField(max_length=300)
    content=models.TextField()
    auther=models.CharField(max_length=40)
    created=models.DateField(auto_now_add=True)
    published=models.BooleanField()
    
    class Meta:
        ordering=['-created']

        def __unicode__(self):
            return u'%s' % self.title

    def get_absolute_url(self):
        return reverse('Auth.views.post',args=[self.slug])

    def __str__(self):
        return self.title

class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Product(models.Model):
    id=models.IntegerField(primary_key=True,unique=True)
    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=200,unique=True)
    detail=models.CharField(max_length=300)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    created=models.DateField(auto_now_add=True)

    class Meta:
        ordering=['-created']

        def __unicode__(self):
            return u'%s' % self.title

    def get_absolute_url(self):
        return reverse('Auth.views.product',args=[self.slug])

    def __str__(self):
        return self.title