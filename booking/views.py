from django.shortcuts import render
from django.views import generic, View

from .models import Booking
# from .forms import CommentForm

# Views

class BookingList(generic.ListView):
    model = Booking
    queryset = Booking.objects.order_by("updated_on")
    template_name = "booking.html"

