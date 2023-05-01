from django.contrib import admin
from  .models import CustomUsers
from items.models import Items, Transaction
# Register your models here.

class ItemsInline(admin.TabularInline):
    model = Items

class TransactionInline(admin.TabularInline):
    model = Transaction

@admin.register(CustomUsers)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username',"email")
    inlines = [ItemsInline, TransactionInline]

