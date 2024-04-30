from rest_framework import serializers
from main.models import ToDoList

class AuthorSerializer(serializers.ModelSerializer):

    """
    Serializing all the Authors
    """

    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name')
