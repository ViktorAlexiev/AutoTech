from rest_framework import serializers
from .models import *

class b_data_Serializer(serializers.ModelSerializer):
    class Meta:
        model = b_data
        fields = '__all__'
        
class c_data_Serializer(serializers.ModelSerializer):
    class Meta:
        model = c_data
        fields = '__all__'
        
class w_data_Serializer(serializers.ModelSerializer):
    class Meta:
        model = w_data
        fields = '__all__'

class p_data_Serializer(serializers.ModelSerializer):
    class Meta:
        model = p_data
        fields = '__all__'