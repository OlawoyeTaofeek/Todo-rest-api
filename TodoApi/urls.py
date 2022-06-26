from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
# Todos
    path('todos/completed', views.TodoCompletedList.as_view()),
    path('todos/completed/<int:pk>', views.TodoCompletedDestroy.as_view()),
    path('todos/', views.TodoCurrentListCreate.as_view()),
    path('todos/<int:pk>', views.TodoRetrieveDestroy.as_view()),
    path('todos/<int:pk>/complete', views.TodoComplete.as_view()),

#Auth
    path('signup', views.SignUp),
    path('get-token', views.login)
]
