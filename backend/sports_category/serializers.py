from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    """разряд"""
    class Meta:
        model = Category
        fields = "__all__"
