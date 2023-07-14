from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email=models.EmailField(unique=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    def __str__(self) -> str:
        return self.email


class Book(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    author=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    
    def __str__(self) -> str:
        return self.title


