from django.db import models

# Create your models here.
class Trip(models.Model):
    buyer = models.CharField(max_length=50)
    date = models.DateField(default='')

    def __str__(self):
        return f"{self.buyer} | {self.date}"