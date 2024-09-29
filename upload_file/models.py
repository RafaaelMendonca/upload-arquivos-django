from django.db import models

class MyFile(models.Model):
    title = models.CharField(max_length=20)
    arq = models.FileField(upload_to="img")

    def __str__(self) -> str:
        return self.title