from django.db import models


# Create your models here.
class Meal(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    notes = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    meals = models.ForeignKey(Meal, related_name='orders')