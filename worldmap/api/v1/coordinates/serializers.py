from rest_framework import serializers

from coordinates import models as coordinates_models


class CoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = coordinates_models.MapObject
        fields = (
            "latitude",
            "longitude",
            "name",
        )
