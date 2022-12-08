from django.contrib import admin
from .models import Cart, Product, Customer

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','Product_image','selling_price','discount_price','category','created_at')
    search_fields = ('title','selling_price','description','category','id')
    list_filter = ('category',)

admin.site.register(Product, ProductAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'city', 'state')
    search_fields = ('name', 'user', 'city')
    list_filter = ('state',)

admin.site.register(Customer, CustomerAdmin)


class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity')
    search_fields = ('product', 'user')

admin.site.register(Cart, CartAdmin)

