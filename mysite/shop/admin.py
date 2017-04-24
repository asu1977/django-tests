from django.contrib import admin
from .models import Product


@admin.register(Product)
class AdminShop(admin.ModelAdmin):
    list_display = ["name", "price"]
