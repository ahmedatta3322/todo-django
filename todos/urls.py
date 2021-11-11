from django.urls import path
from .views import TodosList, SingleTodo, CreateTodo
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('', TodosList.as_view()),
    path('<int:pk>', SingleTodo.as_view()),
    path('todo', CreateTodo.as_view()),
    path('login', obtain_auth_token)
]
