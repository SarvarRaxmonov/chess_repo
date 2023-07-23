from django.db import models
from django.utils.translation import gettext_lazy as _


class Levels(models.TextChoices):
    Beginner = "Beginner", _("Boshlang'ich")
    Intermediate = "Intermediate", _("O'rtacha")
    Advanced = "Advanced", _("Yuqori'")


class Language(models.TextChoices):
    Ru = "Ru", _("Russian")
    Uz = "Uz", _("Uzbek")
    English = "Eng", _("English")


class ComplainTypes(models.TextChoices):
    INAPPROPRIATE_CONTENT = "Inappropriate Content", "Inappropriate Content"
    SPAM = "Spam", "Spam"
    ABUSE = "Abuse", "Abuse"
    OTHER = "Other", "Other"


STATUS_CHOICES = (
    ("pending", "Pending"),
    ("completed", "Completed"),
    ("canceled", "Canceled"),
)

TEXT_CHOICES = (
    ("processing", "Processing"),
    ("shipped", "Shipped"),
    ("delivered", "Delivered"),
    ("canceled", "Canceled"),
)

PAYMENT_CHOICES = (
    ("credit_card", "Credit Card"),
    ("paypal", "PayPal"),
    ("cash_on_delivery", "Cash on Delivery"),
)
