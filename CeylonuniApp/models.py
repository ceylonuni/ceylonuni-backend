from django.db import models

# Create your models here.

class University(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=350)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=350)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    university = models.ForeignKey(
        University, on_delete=models.CASCADE)


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=350)
    lastName = models.CharField(max_length=350)
    email = models.CharField(max_length=150,unique=True)
    mobile = models.IntegerField()
    isVerified = models.BooleanField(default=False)
    isActive = models.BooleanField(default=True)
    address1 = models.CharField(max_length=350)
    address2 = models.CharField(max_length=350,null=True)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    zip = models.IntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    deletedAt = models.DateTimeField(null=True,default=None)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE)


