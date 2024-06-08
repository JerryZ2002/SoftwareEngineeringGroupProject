from django.contrib import admin

# admin.py

from django.contrib import admin
from .models import Product_info,PurchaseOrder,SalesOrder,Inventory


admin.site.register(Product_info)
admin.site.register(PurchaseOrder)
admin.site.register(SalesOrder)
admin.site.register(Inventory)


