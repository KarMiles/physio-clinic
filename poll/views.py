"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.views import generic, View
from django.urls import reverse_lazy, reverse
from django.core.exceptions import PermissionDenied
from django.utils.datastructures import MultiValueDictKeyError
from accounts.views import StaffRequiredMixin

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .forms import CreatePollForm
from .models import Poll


# Poll views

class PollList(generic.ListView):
    """
        A view to show page with a list of polls
        Args:
            ListView: class based view
        Returns:
            Render page with list of polls
        """
    model = Poll
    template_name = "poll/poll_home.html"

    def get_queryset(self):
        return Poll.objects.order_by("id")


class CreatePoll(StaffRequiredMixin, generic.CreateView):
    """
    A view to show form to create a new poll
    Args:
        CreateView: class based view
    Returns:
        Render page with form to create a new poll
        with success message on completion
    """
    template_name = "poll/poll_create.html"
    form_class = CreatePollForm
    success_url = reverse_lazy('poll_home')

    def form_valid(self, form):
        """
        Check user's authorization level,
        Set poll author to self instances,
        Send confirmation message.
        Args:
            self (object): self.
            form (object): form.
        Returns:
            The form
        """
        if not self.request.user.is_staff:
            raise PermissionDenied

        def __init__(self, form):
            self.object = form.instance

        form.instance.author = self.request.user

        response = super().form_valid(form)

        messages.add_message(
            self.request,
            messages.INFO,
            'Poll created successfully!')
        return response

    def get_success_url(self):
        return reverse('poll_vote', args=[self.object.id])


class PollVote(View):
    """
    A view to show form with the poll
    Args:
        View: class based view
    Returns:
        Render page with form to cast a vote
        After vote show success message
        and results on current poll
    """

    def get(self, request, poll_id):
        """
        Get form for chosen poll
        Args:
            self: Self object
            request (object): HTTP Request object
            poll_id: poll_id
        Render:
            Page with poll questions
        """
        queryset = self.get_queryset()
        poll = get_object_or_404(queryset, pk=poll_id)
        context = {
            'poll': poll
        }

        return render(
            request,
            "poll/poll_vote.html",
            context
        )

    def post(self, request, poll_id):
        """
        Posts new vote data for selected poll,
        Redirects to page with poll results
        Args:
            self: Self object
            request (object): HTTP Request object
            poll_id: poll_id
        Render:
            Page with poll results
        """
        queryset = self.get_queryset()
        poll = get_object_or_404(queryset, pk=poll_id)

        vote_checked = True
        try:
            vote_checked = request.POST['poll']
        except MultiValueDictKeyError:
            vote_checked = False

        if vote_checked:

            if self.request.method == 'POST':
                selected_option = request.POST['poll']
                if selected_option == 'option1':
                    poll.option_one_count += 1
                elif selected_option == 'option2':
                    poll.option_two_count += 1
                elif selected_option == 'option3':
                    poll.option_three_count += 1
                else:
                    return HttpResponse(400, 'Invalid form option')

                poll.save()

                messages.add_message(
                        request,
                        messages.INFO,
                        'Thank you for your vote!')

                return redirect('poll_results', poll.id)

            context = {
                'poll': poll
            }

            return render(
                request,
                'poll/poll_vote.html',
                context)

        messages.error(request, "Please choose one option!")
        context = {
            'poll': poll
        }
        return render(
            request,
            'poll/poll_vote.html',
            context)

    def get_queryset(self):
        """
        Get all poll objects
        Args:
            self (object): Self object
        Returns:
            All poll objects
        """
        return Poll.objects.all()

    # Possible next step - show inactive polls to staff
    # def get_queryset(self):
    #     if self.request.user.is_staff:
    #         return Poll.objects.all()
    #     else:
    #         return Poll.objects.filter(status=1)


class PollResults(View):
    """
    A view to show poll results
    Args:
        View: class based view
    Returns:
        Render page with poll results
    """

    def get(self, request, poll_id):
        """
        Gets data on selected poll
        Args:
            self: Self object
            request (object): HTTP Request object
            poll_id: poll_id
        Render:
            Page with poll results
        """
        poll = Poll.objects.get(pk=poll_id)
        context = {
            'poll': poll
        }

        return render(
            request,
            'poll/poll_results.html',
            context)


def poll_delete(request, poll_id):
    '''
    Check if user authorized,
    Delete selected poll,
    Show confirmation message,
    Redirect to poll page.
    Args:
        request (object): HTTP request object
        poll_id: poll_id
    Return:
        Render poll page.
    '''
    if not request.user.is_staff:
        raise PermissionDenied

    polls = Poll.objects.all()
    poll = Poll.objects.get(pk=poll_id)

    if request.method == 'POST':
        poll.delete()
        messages.add_message(
            request,
            messages.INFO,
            'Poll deleted successfully!')
        return redirect('poll_home')

    context = {
        'polls': polls,
        'poll': poll
    }

    return render(request, 'poll/poll_confirm_delete.html', context)
