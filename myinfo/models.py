from django.db import models

class MyInfo(models.Model):
    name = models.CharField(max_length=100, primary_key=True)  # Explicitly set 'name' as the primary key

    class Meta:
        db_table = 'myinfo'  # Use the existing table

    def __str__(self):
        return self.name
