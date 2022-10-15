# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from turtle import mode

from django.db import models

# Create your models here.
class CoinMarketCap(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    latest=models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    _1h_perc = models.CharField(max_length=200)
    _24h_perc = models.CharField(max_length=200)
    _7d_perc = models.CharField(max_length=200)
    market_cap = models.CharField(max_length=200)
    volume_24h = models.CharField(max_length=200)
    circulating_supply = models.CharField(max_length=200)
   