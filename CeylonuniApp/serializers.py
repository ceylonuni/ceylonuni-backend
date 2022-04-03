from pyexpat import model
from rest_framework import serializers
from CeylonuniApp.models import Universities,Courses,Students


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model=Universities
        fields=('id','name','createdAt','updatedAt')

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Courses
        fields=('id','name','createdAt','updatedAt','university')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Students
        fields=('id','firstName','lastName','email','mobile','isVerified','isActive','address1','address2','city','state','zip','createdAt','updatedAt','deletedAt','course')

# class AccountSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Accounts
#         fields=('id','email','password','name','verifiedDate','createdAt','updatedAt','deletedAt','student')