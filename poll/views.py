# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.views import generic, View
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from helpers.views import StaffRequiredMixin
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


class CreatePoll(generic.CreateView):
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
    success_url: reverse_lazy('poll_home')

    def form_valid(self, form):
        self.object = form.instance
        self.object.author = self.request.user
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
        queryset = self.get_queryset()
        poll = get_object_or_404(queryset, pk=poll_id)

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
    
    def get_queryset(self):
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
