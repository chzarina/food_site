from django.contrib import admin
from .models import TableBooking

@admin.register(TableBooking)
class TableBookingAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'date', 'time', 'guests', 'status', 'created_at']
    list_filter = ['status', 'date', 'created_at']
    search_fields = ['name', 'email', 'phone']
    list_editable = ['status']
    date_hierarchy = 'date'

