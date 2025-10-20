from django.db import models
class User(models.Model):
    first_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(unique=True)
    last_name = models.CharField(max_length=150, blank=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.id} ,{self.first_name} , {self.email}"