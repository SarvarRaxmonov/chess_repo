from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from apps.courses.models import Course
from apps.book.models import Book


class Registration(models.Model):
    name = models.CharField(max_length=100)
    phone_number = PhoneNumberField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Profile(models.Model):
    full_name = models.CharField(max_length=200)
    phone_number = PhoneNumberField()
    photo = models.ImageField(upload_to="photos/")
    date_of_birth = models.DateField()

    def __str__(self):
        return self.full_name

    def get_country_code(self):
        return self.phone_number.country_code

    def get_national_number(self):
        return self.phone_number.national_number


class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    phone_number = PhoneNumberField()
    text = models.TextField()
    rules_check = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name


class Liked(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"Liked by {self.user}"
