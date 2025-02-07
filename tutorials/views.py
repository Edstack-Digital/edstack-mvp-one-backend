from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User, Course, Video
from .serializers import CourseSerializer, VideoSerializer

# from django.views.decorators.http import require_POST
# from django.contrib import messages
# from .automations import save_courses, save_videos

# @require_POST
# def save_courses_videos(request, queryset):
#     # Perform the desired action
#     doc="/workspaces/edstack-mvp-one-backend/tutorials/edstack-course-list.txt"
#     save_courses(doc)
#     save_videos(doc)

#     messages.success(request, "The action was performed successfully.")


# Create your views here.
class SecureView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "You are authenticated!"})


class SignupView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        try:
            user= User.objects.create(
                email = data['email'],
                password=make_password(data['password']),
                first_name=data.get('first_name', ''),
                last_name=data.get('last_name', ''),
            )
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# class SignupView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             if user:
#                 json = serializer.data
#                 return Response(json, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class LoginView(TokenObtainPairView):
    pass


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]

class VideoViewSet(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [AllowAny]
