from django.db import models
from apps.common.choices import STATUS_CHOICES, TEXT_CHOICES, PAYMENT_CHOICES
from phonenumber_field.modelfields import PhoneNumberField


class Card(models.Model):
    book = models.ForeignKey("book.Book", on_delete=models.CASCADE)
    user = models.ForeignKey("user.Profile", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)


class Kupon(models.Model):
    promo_code = models.CharField(max_length=100, unique=True)
    expired_date = models.DateField()


class Purchase(models.Model):
    products = models.ManyToManyField(Card)
    order_number = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_cost = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=TEXT_CHOICES)
    kupon = models.ForeignKey(Kupon, on_delete=models.SET_NULL, null=True)
    payment_type = models.CharField(max_length=20, choices=PAYMENT_CHOICES)


class Client(models.Model):
    purchase_id = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    name = models.TextField()
    phone_number = PhoneNumberField()
    email = models.EmailField()

    def __str__(self):
        return self.name
