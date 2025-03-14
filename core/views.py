from rest_framework import viewsets
from django.shortcuts import render
from .models import Job
from .serializers import JobSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

def index(request):
    return render(request, 'core/index.html')
