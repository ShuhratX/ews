from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password

class TrainingCenterDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingCenters
        fields = ('email', 'password', 'name', 'photo', 'phone_number', 'text', 'telegram', 'instagram', 'you_tube', 'languages')
        

    def validate(self, attrs):
        email = attrs.get('email')
        
        if TrainingCenters.objects.filter(email=email).exists():
            raise serializers.ValidationError({
                'error': 'Email is already registered',
                })
        
        return super().validate(attrs)

    def create(self, validated_data):
        user = TrainingCenters.objects.create(
            email=validated_data['email'],
            name = validated_data['name'],
            photo = validated_data['photo'],
            phone_number = validated_data['phone_number'],
            text = validated_data['text'],
            telegram = validated_data['telegram'],
            instagram = validated_data['instagram'],
            you_tube = validated_data['you_tube'],
            languages = validated_data['languages'],

        )
        user.set_password(validated_data['password'])
        user.save()
        return user
     

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingCenters
        fields = ('email', 'password',)


class VerifySerializer(serializers.ModelSerializer):
    kod = serializers.CharField(max_length = 10)
    class Meta:
        model = TrainingCenters
        fields = ('email', 'kod')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = "__all__"


class PayMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayMe
        fields = "__all__"


class TrainingCenterGetSerializer(serializers.ModelSerializer):
    group = GroupSerializer(many=True, required=False)
    students = StudentsSerializer(many=True, required=False)
    subjects = SubjectsSerializer(many=True, required=False)
    teachers = TeacherSerializer(many=True, required=False)
    categories = CategorySerializer(many=True, required=False)

    class Meta:
        model = TrainingCenters
        fields = fields = (
            'id', 
            'email', 
            'name', 
            'photo', 
            'phone_number', 
            'text', 
            'instagram', 
            'telegram', 
            'you_tube',
            'categories',
            'group',
            'students',
            'subjects',
            'teachers'
            )
