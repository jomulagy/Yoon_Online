from django.db import models
from django.contrib.auth.models import AbstractUser	# AbstractUser 불러오기
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    phone_number = PhoneNumberField()
