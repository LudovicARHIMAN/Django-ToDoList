from rest_framework import serializers
from main.models import ToDoList

class ToDoList(serializers.ModelSerializer):
    """
    Serializing all the Authors
    """

    class Meta:
        model = ToDoList
        fields = ('id', 'user', 'name')
