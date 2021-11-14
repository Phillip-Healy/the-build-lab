from django.contrib import admin
from .models import Payment, Content, Product, Price


admin.site.register(Payment)
admin.site.register(Content)


class PriceInlineAdmin(admin.TabularInline):
    model = Price
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [PriceInlineAdmin]


admin.site.register(Product, ProductAdmin)
