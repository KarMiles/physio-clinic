"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.db import models

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.contrib.auth.models import User
from blog.models import Post


# Models for booking app

# Choice options for Booking class
STATUS = ((0, "Pending"), (1, "Closed"))


class Booking(models.Model):
    """
    Class for the booking model
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='booking_user')
    treatment = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='booking_treatment')
    time = models.DateTimeField()
    message = models.TextField()
    status = models.IntegerField(
        choices=STATUS,
        default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        """
        Returns the booking message string
        Args:
            self (object): self.
        Returns:
            The booking message string
        """
        return self.message
