from django.db import models
from apps.common.models import OrdinaryFields


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class News(OrdinaryFields):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/")
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
