from ckeditor.fields import RichTextField
from django.db import models
from apps.common.choices import Levels, ComplainTypes
from apps.common.models import OrdinaryFields
from apps.user.models import Profile


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Course(OrdinaryFields):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/")
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    level = models.CharField(max_length=20, choices=Levels)
    view_count = models.PositiveIntegerField(default=0)
    certificate = models.FileField(upload_to="certificates/", null=True, blank=True)

    def __str__(self):
        return self.title


class Unit(models.Model):
    name = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Video(OrdinaryFields):
    name = models.TextField()
    unit_id = models.ForeignKey(Unit, on_delete=models.CASCADE)
    description = RichTextField()
    video = models.FileField(upload_to="videos/")
    video_link = models.URLField()

    def __str__(self):
        return self.name


class Comment(OrdinaryFields):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f"Comment by {self.user}"


class Complain(models.Model):
    type = models.CharField(max_length=100, choices=ComplainTypes)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"{self.type} Complain on {self.comment}"
