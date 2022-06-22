from django.shortcuts import render
from rest_framework import generics, status, views, permissions
from .serializers import CourseSerializer, StudentSerializer,UniversitySerializer, UniversityEmailSerializer
from rest_framework.response import Response
from .models import Course, University,UniversityEmail
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
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

# create university, list all universities
class UniversityListAPIView(ListCreateAPIView):
    serializer_class=UniversitySerializer
    queryset = University.objects.all()

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return self.queryset.filter()

# update, patch, delete university
class UniversityDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class=UniversitySerializer
    queryset = University.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.filter()

# list all university emails
class UniversityEmailListAPIView(ListCreateAPIView):
    serializer_class=UniversityEmailSerializer
    queryset = UniversityEmail.objects.all()

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return self.queryset.filter()

# update, patch, delete university email
class UniversityEmailDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class=UniversityEmailSerializer
    queryset = UniversityEmail.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.filter()

class CourseListAPIView(ListCreateAPIView):

    serializer_class = CourseSerializer
    
    # def post(self, request):
    #     course = request.data
    #     serializer = self.serializer_class(data=course)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     course_data = serializer.data
    #     return Response(course_data, status=status.HTTP_201_CREATED)

    queryset = Course.objects.all()

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return self.queryset.filter()

class CourseDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class=CourseSerializer
    queryset = Course.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.filter()