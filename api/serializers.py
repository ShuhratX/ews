from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
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