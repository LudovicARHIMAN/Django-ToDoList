from rest_framework import serializers
from main.models import ToDoList, Item


class ToDoListSerializers(serializers.ModelSerializer):
    '''
    Serializing ToDoList
    '''

    class Meta:
        model = ToDoList
        fields = ('id', 'user', 'name')


class ItemSerializers(serializers.ModelSerializer):
    '''
    Serializing Item
    '''
    
    class Meta:
        model = Item
        filds = ('id','')