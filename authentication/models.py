from django.db import models
from CeylonuniApp.models import Students
# Create your models here.


class Accounts(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=150,unique=True)
    password = models.CharField(max_length=350)
    username = models.CharField(max_length=150,unique=True)
    verifiedDate = models.DateTimeField(auto_now_add=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    deletedAt = models.DateTimeField(null=True,default=None)
    student = models.ForeignKey(
       Students, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.email

    # def tokens(self):
    #     refresh = RefreshToken.for_user(self)
    #     return {
    #         'refresh': str(refresh),
    #         'access': str(refresh.access_token)
    #     }
