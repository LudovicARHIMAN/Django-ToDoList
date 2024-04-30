from rest_framework import serializers
from main.models import ToDoList

class AuthorSerializer(serializers.ModelSerializer):

    """
    Serializing all the Authors
    """

    class Meta:
        model = ToDoList
        fields = ('id', 'user', 'name')
