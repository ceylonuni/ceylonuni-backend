from django.shortcuts import render
from rest_framework import generics, status, views, permissions
from .serializers import CourseSerializer, StudentSerializer,UniversitySerializer
from rest_framework.response import Response
# Create your views here.


class Student(generics.GenericAPIView):

    serializer_class = StudentSerializer

    def post(self, request):
        student = request.data
        serializer = self.serializer_class(data=student)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        student_data = serializer.data
        return Response(student_data, status=status.HTTP_201_CREATED)


class University(generics.GenericAPIView):

    serializer_class = UniversitySerializer

    def post(self, request):
        university = request.data
        serializer = self.serializer_class(data=university)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        university_data = serializer.data
        return Response(university_data, status=status.HTTP_201_CREATED)

class Course(generics.GenericAPIView):

    serializer_class = CourseSerializer

    def post(self, request):
        course = request.data
        serializer = self.serializer_class(data=course)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        course_data = serializer.data
        return Response(course_data, status=status.HTTP_201_CREATED)