from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.TemasModel)
class TemasAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nombre_tema",
        "created",
        "updated"
    )

    list_display_links = (
        "id",
        "nombre_tema",
    )

    search_fields = (
        "id",
        "nombre_tema",
    )

    list_filter = (
        "nombre_tema",
    )

    readonly_fields = (
        "created",
        "updated"
    )