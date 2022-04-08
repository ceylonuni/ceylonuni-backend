from pyexpat import model
from rest_framework import serializers
from CeylonuniApp.models import University,Course,Student


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model=University
        fields=('id','name','createdAt','updatedAt')

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=('id','name','createdAt','updatedAt','university')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=('id','firstName','lastName','email','mobile','isVerified','isActive','address1','address2','city','state','zip','createdAt','updatedAt','deletedAt','course')
