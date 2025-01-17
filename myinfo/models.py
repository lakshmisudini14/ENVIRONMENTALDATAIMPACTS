from django.db import models

# Create your models here.
from django.db import models

class MyInfo(models.Model):
    name = models.CharField(max_length=100)

    def _str_(self):
        return self.name