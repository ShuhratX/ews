from django.conf import settings
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *

import random
import pytz
from datetime import datetime
datetime.utcnow().replace(tzinfo=pytz.utc)

class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    @staticmethod
    def post(request):
        serializer = UserSerializer(data=request.data)
        subject = "Emailni tasdiqlash"
        kod     =  str(random.randint(100000, 1000000))
        msg     = "Emailni tasdiqlash uchun bir martalik kod: " + kod
        to      = request.data.get('email')
        res     = send_mail(subject, str(msg), settings.EMAIL_HOST_USER, [to])
        if(res == 1):
            msg1 = str(msg)+" "+  to +" ga jo'natildi "
        else:  
            msg1 = "Mail Sending Failed."
        print(msg1)
        if serializer.is_valid():
            user = serializer.save()
            user.msg = kod
            user.save()

            return Response("Ro'yxatdan o'tish muvaffaqiyatli yakunlandi", status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        try:
            email = request.data.get('email')
            msg = request.data.get('password')
            ver = TrainingCenters.objects.get(email=email)
            if ver and msg==ver.msg:
                ver.verified = True
                ver.msg = ''
                ver.save()
                return Response("Email muvaffaqiyatli tasdiqlandi!")
            else:
                return Response("Email yoki kod noto'g'ri")
        except:
            return Response("Email yoki kod noto'g'ri")

class LoginView(APIView):
    serializer_class = LoginSerializer

    @staticmethod
    def post(request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = auth.authenticate(email=email, password=password)

        if user is not None:
            if user.verified == True:
                user.last_login = datetime.now(pytz.utc)
                user.save()
                return Response({
                    'id': user.id,
                    'email': email
                })
            else:
                return Response("Emailingiz tasdiqlashdan o'tmagan")
        else:
            return Response("Email yoki parol noto'g'ri", status=status.HTTP_400_BAD_REQUEST)
        

