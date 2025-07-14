from django.contrib import admin
from .models import Category, MenuItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price', 'is_available', 'is_featured']
    list_filter = ['category', 'is_available', 'is_featured', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['is_available', 'is_featured']
    prepopulated_fields = {'slug': ('title',)}

