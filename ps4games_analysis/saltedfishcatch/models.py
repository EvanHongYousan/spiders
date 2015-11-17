from django.db import models

# Create your models here.

class Commodity(models.Model):
    price = models.FloatField(max_length=200)
    location = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    href = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return (self.price, self.location, self.title, self.href, self.description)

    def __unicode__(self):
        return (self.price, self.location, self.title, self.href, self.description)
