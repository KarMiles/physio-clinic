from django.db import models
from django.contrib.auth.models import User
from blog.models import Post

STATUS = ((0, "Pending"), (1, "Closed"))


# Models

class Booking(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='booking_user')
    treatment = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='booking_treatment')
    time = models.DateTimeField(blank=True)
    message = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_on']

    def __str__(self):
        return self.message
