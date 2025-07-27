from django.db import models

class Fuchka(models.Model):
    name=models.CharField(max_length=255)
    price=models.FloatField()
    quantity=models.IntegerField()
    image=models.CharField(max_length=2083)

class CartItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    added_at = models.DateTimeField(auto_now_add=True)

