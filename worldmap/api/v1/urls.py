from django.urls import path, include

from api.v1.coordinates import routes

app_name = "api"

urlpatterns = [
    path(
        "coordinates/",
        include(
            (routes.router.urls, "coordinates"),
            namespace="coordinates",
        ),
    ),
]
