# -*- coding: utf-8 -*-

from django.apps import AppConfig

class ScraperConfig(AppConfig):
    name = 'scraper'
    def ready(self):
        from .schedule import start
        start()