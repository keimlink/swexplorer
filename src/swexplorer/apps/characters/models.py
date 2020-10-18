import os

from django.conf import settings
from django.db import models


class Dataset(models.Model):
    path = models.FilePathField(
        path=os.path.join(settings.MEDIA_ROOT, "characters"), match=r".*\.csv$", unique=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return os.path.basename(self.path)
