from django.db import models
from apps.common.models import OrdinaryFields
from apps.common.choices import Levels, Language
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Book(OrdinaryFields):
    title = models.TextField()
    author = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.FloatField(default=0)
    image = models.FileField(upload_to="/images")
    page = models.IntegerField()
    published_date = models.DateField()
    level = models.CharField(max_length=60, choices=Levels)
    category = models.ForeignKey(Category, models.CASCADE)
    language = models.CharField(max_length=50, choices=Language)
    tags = models.ManyToManyField("Tag", blank=True)
    description = RichTextField()


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
