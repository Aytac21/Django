from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return self.name
