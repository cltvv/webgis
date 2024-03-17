from rest_framework.routers import DefaultRouter
from . import views as coordinates_views

app_name = "v1"

router = DefaultRouter()
router.register(
    r"map-objects",
    coordinates_views.CoordinatesListView,
    basename="map-objects",
)
