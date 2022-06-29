from django.shortcuts import render
from django.views import generic, View

from .models import Booking
from .forms import BookingForm


# Views

class BookingList(generic.ListView):
    model = Booking
    queryset = Booking.objects.order_by("updated_on")
    template_name = "booking.html"


class BookingDetail(View):

    def get(self, request, *args, **kwargs):
        queryset = Booking.objects
