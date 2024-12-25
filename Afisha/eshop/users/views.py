import random

from django.contrib.auth.hashers import is_password_usable
from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .models import SMSCode
from .serializers import RegisterSerializer, SMScodeSerializer, UserLoginSerializer
from rest_framework.views import APIView

from rest_framework.authtoken.models import Token

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(
            username=serializer.data['username'],
            email=serializer.data['email'],
            password=serializer.data['password'],
            is_active = False
        )
        code = "".join([str(random.randint(0, 9))for i in range(6)])
        SMSCode.objects.create(user=user, code=code)
        send_mail(
            'Your code',
            message=code,
            from_email='<EMAIL>',
            recipient_list=[user.email],
        )
        return Response(data={'user_id':user.id}, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    def post(self, request):
        serializer =  UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response(data={'key':token.key})
        return Response(status=status.HTTP_401_UNAUTHORIZED, data={'error': 'Invalid user or password'})

class SMSCodeConfirm(APIView):
    def post(self, request):
        serializer = SMScodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        sms_code = serializer.validated_data['code']
        try:
            sms = SMSCode.objects.get(code=sms_code)
        except SMSCode.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Invalid code'})
        sms.user.is_active = False
        sms.user.save()
        sms.delete()
        return Response(status=status.HTTP_200_OK)




