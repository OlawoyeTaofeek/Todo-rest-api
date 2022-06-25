from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('todos/completed', views.TodoCompletedList.as_view()),
    path('todos/completed/<int:pk>', views.TodoCompletedDestroy.as_view()),
    path('todos/list', views.TodoCurrentListCreate.as_view()),
    path('todos/list/<int:pk>', views.TodoRetrieveDestroy.as_view()),
]
