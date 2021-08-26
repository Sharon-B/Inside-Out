from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    """
    Tell the admin which fields to display, search
    and how to order them.
    """
    list_display = (
        'name',
        'category',
        'price',
        'product_code',
        'image',
    )

    search_fields = (
        'name',
        'category',
        'description',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'display_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
