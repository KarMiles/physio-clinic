from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin

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


class BookingDetail(View):

    def get(self, request, booking_id, *args, **kwargs):
        queryset = Booking.objects.filter(status=0)
        bookings = get_object_or_404(queryset, pk=booking_id)

        return render(
            request,
            "booking.html",
            {
                "bookings": bookings,
                "booking_form": BookingForm()
            },
        )

    def post(self, request, booking_id, *args, **kwargs):

        queryset = Booking.objects.filter(status=0)
        booking = get_object_or_404(queryset, pk=Booking.user)

        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking_form.instance.email = request.user.email
            booking_form.instance.name = request.user.username
            booking = booking_form.save(commit=False)
            booking.booking = booking
            booking.save()
        else:
            booking_form = BookingForm()
        
        return render(
            request,
            "booking.html",
            {
                "bookings": bookings,
                "booking_form": BookingForm()
            }
        )