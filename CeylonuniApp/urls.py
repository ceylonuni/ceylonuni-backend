from django.urls import path
from . import views
from .views import Course, Student,University

urlpatterns = [
     path('course/',Course.as_view(),name="course"),
     path('student/',Student.as_view(),name="student"),
     path('university', views.UniversityListAPIView.as_view(), name="Universities"),
     path('university/<int:id>', views.UniversityDetailAPIView.as_view(), name="University"),
     path('universityEmail', views.UniversityEmailListAPIView.as_view(), name="UniversityEmails"),
     path('universityEmail/<int:id>', views.UniversityEmailDetailAPIView.as_view(), name="UniversityEmail"),
    ]

    