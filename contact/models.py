from django.db import models
from django.contrib.auth.models import User


# Models for contact app

STATUS = ((0, "Pending"), (1, "Closed"))

class Contact(models.Model):

    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=320)
    subject = models.CharField(max_length=255)
    body = models.TextField(max_length=3000)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body
