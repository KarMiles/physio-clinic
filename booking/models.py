from django.db import models
from django.contrib.auth.models import User
from blog.models import Post

# Models

class Booking(models.Model):

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
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
    email = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='booking_email')
    # email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-updated_on']
        # email = models.EmailField(email)

    def __str__(self):
        return f"Booking request for {self.treatment} by {self.user}: {self.message}."
