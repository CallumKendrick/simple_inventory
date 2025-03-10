from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name}: {self.quantity}"