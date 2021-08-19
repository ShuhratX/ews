from django.conf import settings
from django.contrib import auth
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.authtoken.models import Token
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
    serializer_class = TrainingCenterDetailSerializer

    @staticmethod
    def post(request):
        serializer = TrainingCenterDetailSerializer(data=request.data)
        subject = "Emailni tasdiqlash"
        kod     =  str(random.randint(100000, 1000000))
        msg     = "Emailni tasdiqlash uchun bir martalik kod: " + kod
        to      = request.data.get('email')
        res     = send_mail(subject, str(msg), settings.EMAIL_HOST_USER, [to])
        if(res == 1):
            msg1 = str(msg)+" "+  to +" ga jo'natildi "
        else:  
            msg1 = "Xabar jo'natishda xatolik!"
        print(msg1)
        if serializer.is_valid():
            user = serializer.save()
            user.msg = kod
            user.save()

            return Response("Ro'yxatdan o'tish muvaffaqiyatli yakunlandi", status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyView(GenericAPIView):
    serializer_class = VerifySerializer

    def post(self, request):
        try:
            email = request.data.get('email')
            msg = request.data.get('kod')
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

class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    @staticmethod
    def post(request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = auth.authenticate(email=email, password=password)

        if user is not None:
            if user.verified == True:
            	token, created = Token.objects.get_or_create(user=user)
            	user.save()
            	return Response({
            		'id': user.id,
            		'email': email,
            		'token': token.key,
            		})
            else:
                return Response("Emailingiz tasdiqlashdan o'tmagan")
        else:
            return Response("Email yoki parol noto'g'ri", status=status.HTTP_400_BAD_REQUEST)
        

class TrainingView(ListAPIView):
    queryset = TrainingCenters.objects.all()
    serializer_class = TrainingCenterGetSerializer

class TrainingDetailView(RetrieveUpdateDestroyAPIView):
    queryset = TrainingCenters.objects.all()
    serializer_class = TrainingCenterGetSerializer


class TeacherView(CreateAPIView, ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class CategoryView(CreateAPIView, ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubjectView(CreateAPIView, ListAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectsSerializer

class SubjectDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectsSerializer


class StudentView(CreateAPIView, ListAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

class StudentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer


class PostView(CreateAPIView, ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer    


class GroupView(CreateAPIView, ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ChatView(CreateAPIView, ListAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

class ChatDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class AttendanceListCreateView(ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


class AttendanceUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


class PayMeListCreateView(ListCreateAPIView):
    queryset = PayMe.objects.all()
    serializer_class = PayMeSerializer


class PayMeUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = PayMe.objects.all()
    serializer_class = PayMeSerializer