# your_app_name/models.py
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Product_info(models.Model):
    product_id = models.IntegerField(primary_key=True, unique=True)
    product_name = models.CharField(max_length=255)
    specification = models.CharField(max_length=255)
    description = models.TextField()
    classification = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product_name
    class Meta:
        db_table = 'product_info'



class PurchaseOrder(models.Model):
    order_number = models.CharField(max_length=50, primary_key=True)
    product_id = models.ForeignKey('Product_info', on_delete=models.CASCADE,db_column='product_id')
    purchase_date = models.DateField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    supplier = models.CharField(max_length=100)
    received = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.order_number} - Product {self.product_id.product_name}"
    
    class Meta:
        db_table = 'purchaseorder'


class SalesOrder(models.Model):
    order_number = models.CharField(max_length=50, primary_key=True)
    product_id = models.ForeignKey('Product_info', on_delete=models.CASCADE,db_column='product_id')
    sales_date = models.DateField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"Order {self.order_number} - Product {self.product_id.product_name}"
    
    class Meta:
        db_table = 'salesorder'


class Inventory(models.Model):
    product_id = models.OneToOneField('Product_info', on_delete=models.CASCADE, primary_key=True,db_column='product_id')
    stock_quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"Inventory for Product {self.product_id.product_name}"
    
    class Meta:
        db_table = 'inventory'
