from django.http import JsonResponse
from rest_framework import generics
from .serializers import TaskSerializer
from .models import Task
from django.shortcuts import render


class TaskView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


def index(request):
    return render(request, "index.html")