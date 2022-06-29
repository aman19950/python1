from django.db import models

# Create your models here.


class user_signup(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=255)
    mobile = models.BigIntegerField()
    gender = models.CharField(max_length=100)

    def __str__(self):
        return self.email
