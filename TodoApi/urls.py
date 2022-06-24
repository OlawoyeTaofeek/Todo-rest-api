from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('todos/completed', views.TodoCompletedList.as_view()),
    path('todos/list', views.TodoCurrentList.as_view()),
    path('todos/list/<int:pk>', views.TodoRetrieveDestroy.as_view()),
]
