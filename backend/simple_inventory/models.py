from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)
    location = models.ForeignKey(
        Location,
        models.SET_NULL,
        null=True
    )

    def __str__(self):
        return f"{self.name}: {self.quantity}"