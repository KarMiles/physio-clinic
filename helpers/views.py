"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Views for error pages

def csrf_failure(request, reason=""):
    """
    View to render 403 error page is called
    for CSRF unauthorized user.
    Args:
        request (object): HTTP request object
        reason: reason
    Returns:
        Render 403 error page
    """
    context = {'message': 'Unauthorized access'}
    return render_to_response('403_csrf.html', context)


def error_403_view(request, _exception):
    """
    View to render 403 error page is called for unauthorized user.
    Args:
        request (object): HTTP request object
        exception: exception error
    Returns:
        Render 403 error page
    """
    return render(request, '403.html', status=403)


def error_404_view(request, _exception):
    """
    View to render 404 error page when non-existent page is called.
    Args:
        request (object): HTTP request object
        exception: exception error
    Returns:
        Render 404 error page
    """
    return render(request, '404.html', status=404)


# def error_500_view(request):
#     """
#     View to render 500 error page in case of server error
#     Args:
#         request (object): HTTP request object
#     Returns:
#         Render 500 error page
#     """
#     return render(request, '500.html', status=500)
#     # return render(request, '500.html')


def error_500_view(request):
    # Return an "Internal Server Error" 500 response code.
    return HttpResponse(status=500)