from django.contrib import admin
from market.models import Customers, Goods, Orders
from .admin_filters import PriceCustomFilter
from .admin_actions import change_quantity

# Register your models here.


@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    all_fields = ('id', 'name', 'email', 'address', 'phone', 'sign_up_date')
    list_display = all_fields
    ordering = all_fields
    list_filter = ('sign_up_date',)
    list_display_links = ('name',)
    readonly_fields = ('id', 'sign_up_date')


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    all_fields = ('id', 'title', 'price', 'total_quantity', 'add_date', 'photo')
    list_display = all_fields
    ordering = all_fields
    list_filter = (PriceCustomFilter, 'add_date')
    list_display_links = ('title',)
    readonly_fields = ('id', 'add_date')
    actions = [change_quantity]


@admin.register(Orders)
class OrderAdmin(admin.ModelAdmin):
    all_fields = ('id', 'user', 'total_price', 'add_date')
    list_display = all_fields
    ordering = all_fields
    list_filter = ('total_price', 'add_date')
    list_display_links = ('id',)
    readonly_fields = ('id', 'add_date')


