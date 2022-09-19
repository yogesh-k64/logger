from django.db import models

# Create your models here.

class Log(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    checked_in = models.DateTimeField(auto_now_add=True)

    def __str__(self):  
        return str(self.checked_in)
