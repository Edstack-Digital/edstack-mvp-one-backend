from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.pagination import PageNumberPagination 
from .models import Course, Video
from .serializers import UserSerializer, CourseSerializer, VideoSerializer

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


class VideoPagination(PageNumberPagination):
    page_size = 10  
    page_size_query_param = 'page_size'  
    max_page_size = 50 

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'num_pages': self.page.paginator.num_pages,
            'num_items_in_page': self.page_size,
            'results': data
        })

# Create your views here.
class SecureView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "You are authenticated!"})


# class SignupView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         data = request.data

#         try:
#             user= User.objects.create(
#                 email = data['email'],
#                 password=make_password(data['password']),
#                 first_name=data.get('first_name', ''),
#                 last_name=data.get('last_name', ''),
#             )
#             return Response({"user": UserSerializer(user).data,
#                              }, status=status.HTTP_201_CREATED)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

User = get_user_model()


class SignupView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh=RefreshToken.for_user(user)
            access_token=str(refresh.access_token)

            if user:
                json = {
                    "access": access_token,
                    "refresh": str(refresh),
                    "user":serializer.data
                }
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user

        data["user"] = UserSerializer(user).data
        return data

class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]

class VideoViewSet(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [AllowAny]
    pagination_class = VideoPagination

