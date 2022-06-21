from django.urls import path
from . import views
from .views import Course, Student,University

urlpatterns = [
     path('course/',Course.as_view(),name="course"),
     path('student/',Student.as_view(),name="student"),
     # path('university/',University.as_view(),name="university"),
     path('university', views.UniversityListAPIView.as_view(), name="Universities"),
     path('university/<int:id>', views.UniversityDetailAPIView.as_view(), name="University"),
    ]

    