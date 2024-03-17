from django.contrib import admin
from . import models


@admin.register(models.MapObject)
class MapObjectAdmin(admin.ModelAdmin):
    list_display = ("name", "latitude", "longitude", "created_at", "updated_at")
    search_fields = ("name",)
    list_filter = ("created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        (None, {"fields": ("name", "latitude", "longitude")}),
        (
            "Даты",
            {
                "fields": ("created_at", "updated_at"),
                "classes": ("collapse",),
            },
        ),
    )
