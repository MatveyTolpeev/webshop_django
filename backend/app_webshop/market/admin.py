from django.contrib import admin
from market.models import Provider, Product, Order, OrderProduct, Consumer, Store, Category
# Register your models here.
class ProviderAdmin(admin.ModelAdmin):
    pass

admin.site.register(Provider, ProviderAdmin)
