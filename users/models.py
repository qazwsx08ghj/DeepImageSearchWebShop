from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    GENDER = (
        ('male', '男'), ('female', '女')
    )

    name = models.CharField("userName", max_length=200, null=True, blank=True)
    b_day = models.DateField("birthday", null=True, blank=True)
    gender = models.CharField("gender", max_length=200, null=True, blank=True)
    phoneNum = models.CharField("phone number", max_length=200, blank=True)
    email = models.EmailField("email", max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = 'Users'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
