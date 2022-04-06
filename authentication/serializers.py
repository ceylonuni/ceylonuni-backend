from pyexpat import model
from rest_framework import serializers
from authentication.models import Accounts
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)

    class Meta:
        model=Accounts
        fields=('id','email','password','username','verifiedDate','createdAt','updatedAt','deletedAt','student')

class AccountVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = Accounts
        fields = ['token']

class EmailSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    class Meta:
        model = Accounts
        fields = ['email']

    # def validate(self, attrs):
    #     email=attrs['email']
    #     validated = True
    #     if validated:
    #         return attrs


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
class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)

    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        user = Accounts.objects.get(email=obj['email'])
        return {
            'access': user.tokens()['access']
        }

    class Meta:
        model = Accounts
        fields = ['email', 'password', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        filtered_user_by_email = Accounts.objects.filter(email=email)
        user = Accounts.objects.filter(email=email, password=password)


        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
       
        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens
        }

        return super().validate(attrs)