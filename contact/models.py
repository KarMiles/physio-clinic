from django.db import models
from django.contrib.auth.models import User

# Models


STATUS = ((0, "Pending"), (1, "Closed"))

class Contact(models.Model):

    name = models.CharField()
    # name = models.ForeignKey(
    #     User,
    #     on_delete=models.CASCADE,
    #     related_name='contact_user')
    email = models.EmailField(max_length=320)
    subject = models.CharField(max_length=255)
    body = models.TextField(required=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body