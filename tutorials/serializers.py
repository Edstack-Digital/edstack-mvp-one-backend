from rest_framework import serializers
from .models import User, Course, Video


# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)
#     class Meta:
#         model = User
#         fields = '__all__'
    
#     def create(self, validated_data):
#         user = User.objects.create_user(
#             email=validated_data['email'],
#             password=validated_data['password'],
#             first_name=validated_data('first_name', ''),
#             last_name=validated_data('last_name', ''),
#         )
#         return user

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
            model = Course
            fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
            model = Video
            fields = '__all__'
