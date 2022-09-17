from django.contrib import admin

from shop.models import Product, Payment, OrderItem, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'code']
    list_editable = []
    list_per_page = 20


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'status', 'amount', 'creation_time']
    list_editable = ['status', 'amount']
    ordering = ['creation_time']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity']
    list_editable = ['product', 'quantity']


admin.site.register(Payment)
