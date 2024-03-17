from django.db import models


class MapObject(models.Model):
    latitude = models.DecimalField(
        verbose_name="широта",
        max_digits=9,
        decimal_places=6,
    )

    longitude = models.DecimalField(
        verbose_name="долгота",
        max_digits=9,
        decimal_places=6,
    )

    name = models.CharField(
        verbose_name="название объекта",
        max_length=256,
    )

    created_at = models.DateTimeField(
        verbose_name="создано",
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        verbose_name="обновлено",
        auto_now=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "объект на карте"
        verbose_name_plural = "объекты на карте"
        ordering = ("-created_at",)
