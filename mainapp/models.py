from django.db import models

class Color(models.Model):
    name = models.CharField(max_length=100)
    hex_value = models.CharField(max_length=7)  # Например, #FFFFFF

    def __str__(self):
        return self.name