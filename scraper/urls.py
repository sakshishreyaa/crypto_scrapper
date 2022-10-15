# Packages
from django.urls import re_path, include

# Modules
from . import views

urlpatterns = [
    re_path(
        r"^get_coin_marketcap/",
        views.get,
        name="",
    ),
    re_path(
        r"^update_coin_marketcap/",
        views.post,
        name="",
    ),
]