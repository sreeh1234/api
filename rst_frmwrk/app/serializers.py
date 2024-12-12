from rest_framework import serializers
from .models import*

class Sample(serializers.Serializer):
    roll_no=serializers.IntegerField()
    name=serializers.CharField()
    age=serializers.IntegerField()
    email=serializers.EmailField()

class Model_serializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields="__all__"   