from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.db.models import CharField, DateField, ImageField, EmailField, BooleanField
from rest_framework.authtoken.views import ObtainAuthToken
from model_utils.fields import StatusField
from model_utils import Choices
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractBaseUser):
    GENDERS = Choices("Male", "Female")
    first_name = CharField(max_length=30, blank=False, null=False)
    last_name = CharField(max_length=150, blank=False, null=False)
    email = EmailField(blank=False, unique=True, null=False)
    password = CharField(max_length=128, blank=False, null=False)
    country_code = CharField(max_length=30, blank=False, null=False)
    phone_number = PhoneNumberField(null=False, unique=True, blank=False)
    gender = StatusField(choices_name="GENDERS", blank=False, null=False)
    birthdate = DateField(blank=False, null=False)
    avatar = ImageField(upload_to='uploads/', blank=False, null=False)
    is_active = BooleanField(default=True)

    USERNAME_FIELD = "email"
    objects = UserManager()

    class Meta:
        verbose_name = ("user")
        verbose_name_plural = ("users")
