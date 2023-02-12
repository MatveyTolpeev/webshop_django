from django.contrib import admin
from market.models import Provider, Product, Order, OrderProduct, Consumer, Store, Category
# Register your models here.
class ProviderAdmin(admin.ModelAdmin):
    pass


class ProductAdmin(admin.ModelAdmin):
    pass


class OrderAdmin(admin.ModelAdmin):
    pass


class OrderProductAdmin(admin.ModelAdmin):
    pass


class ConsumerAdmin(admin.ModelAdmin):
    pass


class StoreAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
admin.site.register(Provider, ProviderAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)
admin.site.register(Consumer, ConsumerAdmin)
admin.site.register(Order, OrderAdmin)