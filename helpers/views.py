# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.shortcuts import render
from django.contrib.auth.mixins import AccessMixin

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Views for error pages

def error_404_view(request, exception):
    """
    View to render 404 error page when non-existent page is called.
    Args:
        request (object): HTTP request object
        exception: exception error
    Returns:
        Render 404 error page
    """
    return render(request, '404.html', status=404)


def error_500_view(request):
    """
    View to render 500 error page in case of server error
    Args:
        request (object): HTTP request object
    Returns:
        Render 500 error page
    """
    return render(request, '500.html', status=500)

# Controlling access

class StaffRequiredMixin(AccessMixin):
    """
    Verify that the current user
    is authenticated as member of staff.
    """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)