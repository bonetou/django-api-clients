from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=False, max_length=40)
    id_number = models.CharField(max_length=11, unique=True)
    phone_number = models.CharField(max_length=14)
    active = models.BooleanField()

    def __str__(self) -> str:
        return self.name
