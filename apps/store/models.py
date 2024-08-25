from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    author_name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
