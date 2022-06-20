from django.urls import path
from .views import LoginAPIView, RegisterView, VerifyAccount, VerifyEmail

urlpatterns = [
    path('register/',RegisterView.as_view(),name="register"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('account-verify/', VerifyAccount.as_view(), name="account-verify"),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
    ]

    