from django.contrib import admin

from .models import Dataset


class DatasetAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    list_display = ("__str__", "created_at")
    search_fields = ["path"]


admin.site.register(Dataset, DatasetAdmin)
