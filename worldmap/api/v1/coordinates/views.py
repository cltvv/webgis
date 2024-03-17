from rest_framework import viewsets, mixins, permissions

from coordinates import models as coordinates_models

from . import serializers


class CoordinatesListView(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = coordinates_models.MapObject.objects.all()
    serializer_class = serializers.CoordinatesSerializer
    permission_classes = [permissions.AllowAny]
