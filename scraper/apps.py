# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig

class ScraperConfig(AppConfig):
    name = 'scraper'
    def ready(self):
    # importing model classes
        print('ji')
        # from .cron import job 
        # job()
    