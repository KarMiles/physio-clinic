"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib import messages

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .models import Booking
from .forms import BookingForm


# Views for booking app

class BookingList(LoginRequiredMixin, generic.ListView):
    """
    A view to show booking messages
    Args:
        LoginRequiredMixin (show only to authorized users)
        ListView: class based view
    Returns:
        Render of booking messages
    """
    model = Booking
    template_name = "booking.html"
    context_object_name = 'bookings'

    def get_queryset(self):
        """
        Filters bookings by the query
        Args:
            self (object): Self object
        Returns:
            bookings with status 0 (pending)
            ordered by creation time
        """
        return Booking.objects.filter(
            status=0,
            user=self.request.user
            ).order_by("created_on")

    def get(self, *args, **kwargs):
        """
        Renders page with bookings list
        Args:
            self (object): Self object
            **kwargs: **kwargs
        Returns:
            Render booking page
        """
        return render(
            self.request,
            "booking.html",
            {
                "bookings": self.get_queryset(),
                "booking_form": BookingForm()
            },
        )

    def post(self):
        """
        A view to save data gathered in booking form
        and show confirmation message.
        Args:
            self (object): Self object
        Returns:
            Save data, show confirmation message,
            redirect to booking page after booking submit.
        """
        booking_form = BookingForm(data=self.request.POST)

        if booking_form.is_valid():
            booking_form.instance.user = self.request.user
            booking_form.save()
            messages.add_message(
                self.request,
                messages.INFO,
                'Booking request submitted!  We will respond shortly.')
            return redirect(reverse('booking'))

        else:
            return render(
                self.request,
                "booking.html",
                {
                    "bookings": self.get_queryset(),
                    "booking_form": booking_form
                }
            )
