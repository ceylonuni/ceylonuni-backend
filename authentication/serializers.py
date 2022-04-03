from pyexpat import model
from rest_framework import serializers
from authentication.models import Accounts


class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)

    class Meta:
        model=Accounts
        fields=('id','email','password','username','verifiedDate','createdAt','updatedAt','deletedAt','student')

    # def validate(self, attrs):
    #     email = attrs.get('email', '')
    #     username = attrs.get('username', '')
    #     student = attrs.get('student', '')
    #     verifiedDate = attrs.get('verifiedDate', '')
         
    #     if not username.isalnum():
    #         raise serializers.ValidationError(
    #             self.default_error_messages)
    #     return attrs

    # def create(self, validated_data):
    #     return Accounts.objects.create_user(**validated_data)