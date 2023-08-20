from django.db import models

class Product(models.Model):
    product_id = models.AutoField
    product_name=models.CharField(max_length=100)
    product_desc=models.CharField(max_length=300)
    product_pub_date=models.DateField()
    