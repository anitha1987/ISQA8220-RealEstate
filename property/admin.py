from django.contrib import admin

from .models import Customer
from .models import Properties


# Registering the customer model

class CustomerList(admin.ModelAdmin):
    list_display = ('name', 'city', 'cell_phone')
    list_filter = ('name', 'city')
    search_fields = ('name', 'city')
    ordering = ['name']


admin.site.register(Customer)


# Registering the property model

class PropertiesList(admin.ModelAdmin):
    list_display = ('type', 'purpose', 'image')
    list_filter = ('type', 'price' )
    search_fields = ('type', 'price', 'purpose')
    ordering = ['type']

admin.site.register(Properties)