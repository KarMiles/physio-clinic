from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from .models import Booking
from .forms import BookingForm


# Views

class BookingList(LoginRequiredMixin, generic.ListView):
    model = Booking
    # queryset = Booking.objects.filter(status=0).order_by("updated_on")
    template_name = "booking.html"
    context_object_name = 'bookings'

    def get_queryset(self):
        return Booking.objects.filter(status=0, user=self.request.user).order_by("updated_on")


# class BookingDetail(View):

    def get(self, *args, **kwargs):
        # queryset = Booking.objects.filter(status=0)
        # bookings = get_object_or_404(queryset, pk=booking_id)

        return render(
            self.request,
            "booking.html",
            {
                # "bookings": bookings,
                "bookings": self.get_queryset(),
                "booking_form": BookingForm()
            },
        )

    def post(self, *args, **kwargs):

        # queryset = Booking.objects.filter(status=0)
        # booking = get_object_or_404(queryset, pk=Booking.user)

        booking_form = BookingForm(data=self.request.POST)
        if booking_form.is_valid():
            booking_form.instance.user = self.request.user
            booking = booking_form.save()
            return redirect(reverse('booking'))
        else:
            # booking_form = BookingForm()
        
            return render(
                self.request,
                "booking.html",
                {
                    # "bookings": bookings,
                    "bookings": self.get_queryset(),
                    # "booking_form": BookingForm()
                    "booking_form": booking_form
                }
            )
