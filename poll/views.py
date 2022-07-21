from django.shortcuts import render, redirect

from .forms import CreatePollForm
from .models import Poll


# Poll views

def poll_home(request):
    polls = Poll.objects.all()
    context = {
        'polls': polls
    }
    return render(request, 'poll/poll_home.html', context)

def poll_create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('poll_home')
    else:
        form = CreatePollForm()
    context = {'form': form}
    return render(request, 'poll/poll_create.html', context)

def poll_results(request, poll_id):
    context = {}
    return render(request, 'poll/poll_results.html', context)

def poll_vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {
        'poll': poll
    }
    return render(request, 'poll/poll_vote.html', context)
