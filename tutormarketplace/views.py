from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .serializers import TutorSerializer
from .models import Tutor


# Create your views here.
def create_tutor(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        courses = request.POST.get('courses')
        badge = request.POST.get('badge')
        rating = request.POST.get('rating')
        phone = request.POST.get('phone')
        image = request.POST.get('image')

        tutor = Tutor.objects.create(first_name=first_name, last_name=last_name, email=email, courses=courses, badge=badge, rating=rating, phone=phone, image=image)
        return JsonResponse({'message': 'Tutor created successfully!', 'tutor_id': tutor.id})
    

class TutorViewSet(ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer
    permission_classes = [IsAuthenticated]
