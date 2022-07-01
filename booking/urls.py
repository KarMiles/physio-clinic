from . import views
from django.urls import path


urlpatterns = [
    # path("booking", views.BookingList.as_view(), name="booking"),
    path('<int:booking_id>/' views.BookingList.as_view(), name="booking")
]
