from rest_framework import generics
from rest_framework import permissions
from .serializers import TodoSerializer, TodoCompleteSerializer
from TodoApp.models import Todo
from django.utils import timezone


# Create your views here.

# List All Possible Completed Todo's
class TodoCompletedList(generics.ListAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user, datecompleted__isnull=False).order_by('-datecompleted')

# List All Possible UnCompleted Todo's
class TodoCurrentListCreate(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user, datecompleted__isnull=True)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Retrieve, Update and Delete all Possible UnCompleted Todo's
class TodoRetrieveDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user, datecompleted__isnull=True)

    def delete(self, request, *args, **kwargs):
        todo = Todo.objects.filter(pk = self.kwargs['pk'], user=self.request.user, datecompleted__isnull=True)
        if todo.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError('This isn\'t your todo so you cant delete it')

# Retrieve and Delete all Possible Completed Todo's
class TodoCompletedDestroy(generics.RetrieveDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user, datecompleted__isnull=False)

# Add Completed to a to do if not completed 
class TodoComplete(generics.UpdateAPIView):
    serializer_class = TodoCompleteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)

    def perform_update(self, serializer):
        serializer.instance.datecompleted = timezone.now()
        serializer.save()
