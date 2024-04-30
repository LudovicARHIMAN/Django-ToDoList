from rest_framework import serializers
from main.models import ToDoList, Item


class ToDoListSerializer(serializers.ModelSerializer):
    '''
    Serializing ToDoList
    '''

    class Meta:
        model = ToDoList
        fields = ('id', 'user', 'name')


class ItemSerializer(serializers.ModelSerializer):
    '''
    Serializing Item
    '''
    
    class Meta:
        model = Item
        fields = ('id','text','complete')