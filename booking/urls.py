from . import views
from django.urls import path


urlpatterns = [
    path("", views.BookingList.as_view(), name="booking"),
]
