from __future__ import unicode_literals

from django.db import models


# Create your models here.
class  art(models.Model):
   url =models.CharField(max_length=200,default=' ')
   content=models.CharField(max_length=1000,default=' ')