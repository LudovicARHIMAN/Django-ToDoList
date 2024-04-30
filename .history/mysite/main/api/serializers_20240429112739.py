from rest_framework import serializers
from main.models import ToDoList, Item


class ToDoList(serializers.ModelSerializer):
    """
    Serializing ToDoList
    """

    class Meta:
        model = ToDoList
        fields = ('id', 'user', 'name')
        