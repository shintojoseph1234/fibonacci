# django imports
from django.contrib.auth.models import User
from .models import FibonacciModel

# REST imports
from rest_framework import serializers


class FibonacciSerializer(serializers.ModelSerializer):
    class Meta:
        model = FibonacciModel
        fields = '__all__'
        depth = 2
