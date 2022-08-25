# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from blog.views import StaffRequiredMixin
from django.views import generic, View
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

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
            Render page with list of polls and context
        """

    model = Poll
    template_name = "poll/poll_home.html"

    def get_queryset(self):

        return Poll.objects.order_by("id")


def poll_create(request):
    """
    A view to show form to create a new poll
    Args:
        request (object): HTTP request object
    Returns:
        Render page with form to create a new poll
        with success message and context
    """
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            messages.add_message(
                request,
                messages.INFO,
                'Poll created successfully!')
            return redirect('poll_home')
    else:
        form = CreatePollForm()
    context = {
        'create_poll_form': CreatePollForm()
        }
    return render(request, 'poll/poll_create.html', context)


def poll_vote(request, poll_id):
    """
    A view to show form with the poll
    Args:
        request (object): HTTP request object
        poll_id: poll_id
    Returns:
        Render page with form to create a new poll
        with success message and context
    """
    poll = Poll.objects.get(pk=poll_id)
    
    if request.method == 'POST':
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

    return render(request, 'poll/poll_vote.html', context)

class PollResults(View):
    """
    A view to show poll results
    Args:
        View: class based view
    Returns:
        Render page with poll results
    """

    def get(self, request, poll_id):

        poll = Poll.objects.get(pk=poll_id)
        context = {
            'poll': poll
        }
        
        return render(
            request,
            'poll/poll_results.html',
            context)

class DeletePoll(StaffRequiredMixin, generic.DeleteView):
    """
    A view to delete a post
    Args:
        StaffRequiredMixin
        DeleteView: generic class based view
    Returns:
        Request confirmation of poll deletion
        Redirect to poll list after delete
    """
    success_url = reverse_lazy('poll_home')
    queryset = Poll.objects.all()
    template_name = 'poll/poll_confirm_delete.html'
    pk_url_kwarg = 'poll_id'

    def poll_delete(self):
        """
        Call the delete() method on the fetched object,
        then redirect to the success URL
        and show confirmation message.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()

        messages.add_message(
            self.request,
            messages.INFO,
            'Poll deleted successfully!')
        
        return HttpResponseRedirect(success_url)
