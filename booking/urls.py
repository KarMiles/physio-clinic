from . import views
from django.urls import path


urlpatterns = [
    path(
        "booking",
        views.BookingList.as_view(),
        name="booking"),
]
