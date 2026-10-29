from django.db import models

# Create your models here.

class ContactModel(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone_no=models.CharField(max_length=10)
    message=models.TextField()


    def __str__(self):
        return f"{self.name}'s message"