from django.db import models
from datetime import datetime
import os


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    date = models.DateTimeField(default=datetime.now, blank=True)

    def extension(self):
        name, extension = os.path.splitext(self.docfile.name)
        return extension

    def delete(self, *args, **kwargs):
        self.docfile.delete()
        super().delete(*args, **kwargs)
