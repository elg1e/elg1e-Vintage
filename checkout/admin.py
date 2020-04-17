from django.contrib import admin
from .models import Order, OrderLineitem

# Register your models here.

class OrderLineAdminInLine(admin.TabularInline):
    model = OrderLineitem

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInLine, )

admin.site.register(Order, OrderAdmin)