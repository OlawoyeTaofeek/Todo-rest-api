from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('todos/completed', views.TodoCompletedList.as_view()),

]
