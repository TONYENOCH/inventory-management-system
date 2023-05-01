from django.contrib import admin
from .models import Items, Transaction
# Register your models here.


@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Items._meta.get_fields()]

@admin.register(Transaction)
class TransationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Transaction._meta.get_fields()]
