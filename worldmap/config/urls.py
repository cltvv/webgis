from django.contrib import admin
from django.urls import path, include

from api.v1 import urls as v1_urls

app_name = "config"

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/v1/",
        include(
            v1_urls,
        ),
    ),
]
