from django.urls import include, path
from rest_framework import routers
from .views import MealViewSet, RatingViewSet, Users_list

router = routers.DefaultRouter()
router.register("meal", MealViewSet)
router.register("rate", RatingViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("user/", Users_list.as_view()),
]
