from rest_framework import serializers

from TodoApp.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    datecompleted = serializers.ReadOnlyField()

    class Meta:
        model = Todo
        fields = ['id', 'title', 'memo', 'created', 'datecompleted', 'important']
        ordering = ['-created']
