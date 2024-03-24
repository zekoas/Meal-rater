from django.contrib import admin
from .models import Meal, Rating


# Register your models here.
class RatingAdmin(admin.ModelAdmin):
    list_display = ["id", "meal", "user", "stars"]
    list_filter = ["meal", "user"]


class MealAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description"]
    list_filter = ["title"]
    search_fields = ["title"]


admin.site.register(Meal, MealAdmin)
admin.site.register(Rating, RatingAdmin)
