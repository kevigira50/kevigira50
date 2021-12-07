from django.contrib import admin
from .models import Product
# Register your models here.
class IdafarmuserAdmin (admin.ModelAdmin):
    list_display = ['phoneNumber','names']
    search_fields = ['phoneNumber']

admin.site.register(Product)
