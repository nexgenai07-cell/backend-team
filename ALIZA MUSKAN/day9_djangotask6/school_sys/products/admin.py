from django.contrib import admin
from .models import Product
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Product Admin Configuration
    """

    list_display = (
        'id',
        'name',
        'price',
        'stock',
        'category'
    )
    list_filter = ('category', 'stock')
    search_fields = ('name',)