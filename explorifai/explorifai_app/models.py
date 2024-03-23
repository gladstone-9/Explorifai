from django.db import models

# Create your models here.
# Models for Explorifai
'''
- Person object when thy login, can implement this later.
- Location object
    - lat
    - long
    - title
    - address
    - description (AI generated historical significant)
'''

class Location(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    description = models.CharField(max_length=400, default="")
    lat = models.DecimalField(decimal_places=25, max_digits=25)
    long = models.DecimalField(decimal_places=25, max_digits=25)

    def __str__(self):
        return self.title