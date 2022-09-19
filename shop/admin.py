from django.contrib import admin

from shop.models import Product, Payment, OrderItem, Order, Shop, Category


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


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'category_url', 'category_id']
    list_editable = []


class ShopAdmin(admin.ModelAdmin):
    list_display = ['shop_name', 'shop_url', 'shop_id']
    list_editable = []


admin.site.register(Payment)
admin.site.register(Category)
admin.site.register(Shop)
