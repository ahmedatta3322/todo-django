from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .serialzers import TodoSerialzer
from .models import Todo
# Create your views here.


class TodosList(generics.ListAPIView):
    serializer_class = TodoSerialzer
    queryset = Todo.objects.all()
    permission_classes = [IsAuthenticated]


class SingleTodo(generics.RetrieveAPIView):
    serializer_class = TodoSerialzer
    queryset = Todo.objects.all()
    permission_classes = [IsAuthenticated]


class CreateTodo(generics.CreateAPIView):
    serializer_class = TodoSerialzer
    permission_classes = [IsAuthenticated]
