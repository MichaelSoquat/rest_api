from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from todo.serializers import TodoSerializer
from .models import Todo
# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
