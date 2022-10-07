from django.conf import settings
from django.db import models

# Create your models here.

class product(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to="images")
    description = models.CharField(max_length=250)

    def __str__(self) -> str:
        return str(self.name)


