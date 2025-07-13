from django.contrib import admin
from .models import Category, MenuItem, Review, Booking

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['Category_name', 'created_at']
    search_fields = ['Category_name']
    ordering = ['Category_name']

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['Item_name', 'category', 'Price', 'is_available', 'created_at']
    list_filter = ['category', 'is_available', 'created_at']
    search_fields = ['Item_name', 'description']
    ordering = ['Item_name']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['User_name', 'Rating', 'created_at']
    list_filter = ['Rating', 'created_at']
    search_fields = ['User_name', 'Description']
    ordering = ['-created_at']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'persons', 'date', 'time', 'created_at']
    list_filter = ['date', 'time', 'created_at']
    search_fields = ['name', 'email', 'phone']
    ordering = ['-created_at']
