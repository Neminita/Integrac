from django.contrib import admin
from .models import Task, Product, Order, OrderProduct

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("created", )

# Register your models here.
admin.site.register(Task, TaskAdmin)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderProduct)