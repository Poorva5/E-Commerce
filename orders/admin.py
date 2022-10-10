from django.contrib import admin
from .models import OrderItem, Order

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name','address', 'postal_code', 'city', 'payment_mode', 'created', 'updated']

    list_filter = ['payment_mode', 'created', 'updated']

    inline = [OrderItemInline]

# Register your models here.
