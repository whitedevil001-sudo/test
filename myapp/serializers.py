from .models import test 
from rest_framework import serializers
class testserializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model=test
        feilds="__all__"