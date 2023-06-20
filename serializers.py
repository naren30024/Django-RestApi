from rest_framework import serializers
from .models import *



class registersSerializer(serializers.ModelSerializer):
    class Meta:
        model=registers
        fields='__all__'