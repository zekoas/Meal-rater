from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import status
from .serializer import MealSerializer, RatingSerializer, UserSerializer
from .models import Rating, Meal
from django.http import request
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    AllowAny,
)
from rest_framework.authtoken.models import Token


# Create your views here.


class Users_list(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            print(token)
            return Response(token.key, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @action(methods=["POST"], detail=True)
    def rate_meal(self, request, pk=None):
        meal = Meal.objects.get(pk=pk)
        user = request.user
        if "stars" in request.data:
            try:  # update
                rate = Rating.objects.get(user=user.id, meal=meal.id)
                rate.stars = request.data["stars"]
                rate.save()
                serializer = RatingSerializer(rate, many=False)
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            except:
                rate = Rating.objects.create(
                    user=user, meal=meal, stars=request.data["stars"]
                )
                serializer = RatingSerializer(rate, many=False)
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(
                {"msg": "Stars not found"}, status=status.HTTP_400_BAD_REQUEST
            )


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        return Response(
            {"msg": "Not the proper way for updating"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def create(self, request, *args, **kwargs):
        return Response(
            {"msg": "Not the proper way for creating"},
            status=status.HTTP_400_BAD_REQUEST,
        )
