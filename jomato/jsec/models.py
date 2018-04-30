# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Stall(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    photourl = models.URLField(max_length=200, blank=True, default='')
    description = models.TextField(blank=True, default='')
class Review(models.Model):
    review = models.TextField(blank=True, default='')
    stall_id = models.IntegerField(blank=True, default=0)
    name = models.CharField(max_length=100, blank=True, default='')
class Rating(models.Model):
	Rating = models.IntegerField()
	stall_id = models.IntegerField(blank=True, default=0)
	name = models.CharField(max_length=100, blank=True, default='')