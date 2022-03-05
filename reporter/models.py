from __future__ import unicode_literals
from django.db.models import Manager as GeoManager
from django.contrib.gis.db import models


# Create your models here.
class Incidences(models.Model):
    name = models.CharField(max_length=32)
    location = models.PointField(srid=4326)
    objects = GeoManager()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Incidences"
