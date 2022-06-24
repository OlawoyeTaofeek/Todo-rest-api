from rest_framework import generics
from rest_framework import permissions
from .serializers import TodoSerializer
from TodoApp.models import Todo


# Create your views here.

class TodoCompletedList(generics.ListAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user, datecompleted__isnull=False).order_by('-datecompleted')

class TodoCurrentList(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user, datecompleted__isnull=True).order_by('-datecompleted')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TodoRetrieveDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    serializer = TodoSerializer(queryset, many=True)
    permission_class = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        todo = Todo.objects.filter(pk = self.kwargs['pk'], user=self.request.user, datecompleted__isnull=True)
        if todo.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError('This isn\'t your todo so you cant delete it')
