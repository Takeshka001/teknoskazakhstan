from django.db import models


class ColorsRalClassic(models.Model):
    bgcolor = models.CharField(max_length=20, blank=True, null=True)
    ral_code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    cmyk_coated = models.CharField(max_length=50, blank=True, null=True)
    cmyk_uncoated = models.CharField(max_length=50, blank=True, null=True)
    hex_code = models.CharField(max_length=7, blank=True, null=True)  # Assuming hex code like "#FFFFFF"
    rgb = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name
    
from django.db import models

class ColorsNcs(models.Model):
    bgcolor = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=100)
    value1 = models.CharField(max_length=50, blank=True, null=True)
    value2 = models.CharField(max_length=50, blank=True, null=True)
    value3 = models.CharField(max_length=50, blank=True, null=True)
    value4 = models.CharField(max_length=50, blank=True, null=True)
    hex_code = models.CharField(max_length=7, blank=True, null=True)  # Assuming hex code like "#FFFFFF"
    r = models.IntegerField(blank=True, null=True)
    g = models.IntegerField(blank=True, null=True)
    b = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

class ColorsPantone(models.Model):
    bgcolor = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=100)
    value1 = models.CharField(max_length=50, blank=True, null=True)
    value2 = models.CharField(max_length=50, blank=True, null=True)
    value3 = models.CharField(max_length=50, blank=True, null=True)
    value4 = models.CharField(max_length=50, blank=True, null=True)
    hex_code = models.CharField(max_length=7, blank=True, null=True)  # Assuming hex code like "#FFFFFF"
    r = models.IntegerField(blank=True, null=True)
    g = models.IntegerField(blank=True, null=True)
    b = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

class ColorsRalDesign(models.Model):
    bgcolor = models.CharField(max_length=20, blank=True, null=True)
    ral_id = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    cymk = models.CharField(max_length=50, blank=True, null=True)
    rgb_percentage = models.CharField(max_length=50, blank=True, null=True)
    hex_code = models.CharField(max_length=7, blank=True, null=True)  # Assuming hex code like "#FFFFFF"
    rgb_values = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name

class ColorsRalEffect(models.Model):
    bgcolor = models.CharField(max_length=20, blank=True, null=True)
    ral_id = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    cymk = models.CharField(max_length=50, blank=True, null=True)
    rgb_percentage = models.CharField(max_length=50, blank=True, null=True)
    hex_code = models.CharField(max_length=7, blank=True, null=True)  # Assuming hex code like "#FFFFFF"
    rgb_values = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name

