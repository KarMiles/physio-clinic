# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .forms import NewUserForm
from django.contrib.auth.mixins import AccessMixin


def register_request(request):
    """
    A view to show registration form for a new user
    Args:
        request (object): HTTP request object.
    Returns:
        Render the registration form with confirmation message
    """
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("main:homepage")
        messages.error(
            request,
            "Unsuccessful registration. Invalid information.")
    form = NewUserForm()

    return render(
        request=request,
        template_name="account/signup.html",
        context={"register_form": form}
        )


# Access management

class StaffRequiredMixin(AccessMixin):
    """
    Verify that the current user
    is authenticated as member of staff.
    """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)