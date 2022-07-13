from django.db import models
from django.contrib.auth.models import User

# Models


STATUS = ((0, "Pending"), (1, "Closed"))

class Contact(models.Model):

    name = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='contact_user')
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

