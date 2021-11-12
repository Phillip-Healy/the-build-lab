from django.contrib import admin
from .models import Customer, Payment, Content


admin.site.register(Payment)
admin.site.register(Content)


# Define admin class for Customer
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'premium')


# Register the admin class and associated model
admin.site.register(Customer, CustomerAdmin)
