from django.urls import path
from .views import Course, Student,University

urlpatterns = [
     path('course/',Course.as_view(),name="course"),
     path('student/',Student.as_view(),name="student"),
     path('university/',University.as_view(),name="university"),
    ]

    