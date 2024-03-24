from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Rating, Meal


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True, "required": True}}


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = "__all__"


class RatingSerializer(serializers.ModelSerializer):
    meal = serializers.StringRelatedField()
    user = serializers.StringRelatedField()

    class Meta:
        model = Rating
        fields = ("id", "stars", "meal", "user")
