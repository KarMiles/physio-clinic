from django.shortcuts import render, get_object_or_404
from django.views import generic, View

from .models import Booking
from .forms import BookingForm


# Views


class BookingList(generic.ListView):
    model = Booking
    queryset = Booking.objects.filter(status=0).order_by("updated_on")
    template_name = "booking.html"


class BookingDetail(View):

    def get(self, request, *args, **kwargs):
        queryset = Booking.objects.filter(status=0)
        booking = get_object_or_404(queryset, booking_id=booking_id)
        
        return render(
            request,
            "booking.html",
            {
                "booking": booking,
                "booking_form": BookingForm()
            },
        )

    def post(self, request, booking_id, *args, **kwargs):

        queryset = Booking.objects.filter(status=0)
        post = get_object_or_404(queryset, booking_id=booking_id)

        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking_form.instance.email = request.user.email
            booking_form.instance.name = request.user.username
            booking = booking_form.save(commit=False)
            booking.booking = booking
            comment.save()
        else:
            booking_form = BookingForm()
        
        return render(
            request,
            "booking.html",
            {
                "booking": booking,
                "booking_form": BookingForm()
            }
        )