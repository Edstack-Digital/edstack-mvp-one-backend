from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Course, Video

User=get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = '__all__'
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
            model = Course
            fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
            model = Video
            fields = '__all__'
