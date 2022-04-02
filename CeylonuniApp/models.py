from django.db import models

# Create your models here.

class Universities(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=350)
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()

class Courses(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=350)
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()
    university = models.ForeignKey(
        Universities, on_delete=models.CASCADE)

class Address(models.Model):
    id = models.AutoField(primary_key=True)
    address1 = models.CharField(max_length=350)
    address2 = models.CharField(max_length=350)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    zip = models.IntegerField()
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()
    deletedAt = models.DateTimeField()

class Students(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=350)
    lastName = models.CharField(max_length=350)
    email = models.CharField(max_length=150)
    mobile = models.IntegerField()
    isVerified = models.BooleanField(default=False)
    isActive = models.BooleanField(default=True)
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()
    deletedAt = models.DateTimeField()
    course = models.ForeignKey(
        Courses, on_delete=models.CASCADE)
    address = models.ForeignKey(
        Address, on_delete=models.CASCADE)

class Accounts(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=350)
    name = models.CharField(max_length=150)
    verifiedDate = models.DateTimeField()
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()
    deletedAt = models.DateTimeField()
    student = models.ForeignKey(
        Students, on_delete=models.CASCADE)


