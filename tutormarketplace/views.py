from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .serializers import TutorSerializer
from tutorials.models import User
from .models import Tutor


# Create your views here.
def create_tutor(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        courses = request.POST.get('courses')
        badge = request.POST.get('badge')
        rating = request.POST.get('rating')
        phone = request.POST.get('phone')
        image = request.POST.get('image')

        user = User.objects.get(id=user_id)
        tutor = Tutor.objects.create(user=user, courses=courses, badge=badge, rating=rating, phone=phone, image=image)
        return JsonResponse({'message': 'Tutor created successfully!', 'tutor_id': tutor.id})
    

class TutorViewSet(ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer
    permission_classes = [IsAuthenticated]