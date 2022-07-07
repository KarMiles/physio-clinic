from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from .models import Booking
from .forms import BookingForm


# Views

class BookingList(LoginRequiredMixin, generic.ListView):
    model = Booking
    template_name = "booking.html"
    context_object_name = 'bookings'

    def get_queryset(self):
        return Booking.objects.filter(status=0, user=self.request.user).order_by("updated_on")

    def get(self, *args, **kwargs):

        return render(
            self.request,
            "booking.html",
            {
                "bookings": self.get_queryset(),
                "booking_form": BookingForm()
            },
        )

    def post(self, *args, **kwargs):

        booking_form = BookingForm(data=self.request.POST)
        if booking_form.is_valid():
            booking_form.instance.user = self.request.user
            booking = booking_form.save()
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
