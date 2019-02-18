from django.db import models

# Create your models here.

class Topic(models.Model):
    top_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.top_name

class WebPage(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE,)
    name = models.CharField(max_length=255, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(WebPage,on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)

#Create models for users

class Users(models.Model):
        first_name = models.CharField(max_length=255)
        last_name = models.CharField(max_length=255)
        email = models.EmailField(max_length=255, unique=True)

        def __self__(self):
            self.first_name = first_name
            self.last_name = last_name
            self.email = email

class Register(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)

    def __self__(self):
            self.first_name = first_name
            self.last_name = last_name
            self.email = email
