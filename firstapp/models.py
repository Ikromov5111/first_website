from django.db import models

# Create your models here.

class Check(models.Model):
    name = models.CharField(max_length=60)
    sms = models.TextField()

    def __str__(self):
        return self.name