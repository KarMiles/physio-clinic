from django.shortcuts import render
from .forms import CreatePollForm

# Poll views

def poll_home(request):
    context = {}
    return render(request, 'poll/poll_home.html', context)

def poll_create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
    else:
        form = CreatePollForm()
    context = {'form': form}
    return render(request, 'poll/poll_create.html', context)

def poll_results(request):
    context = {}
    return render(request, 'poll/poll_results.html', context)

def poll_vote(request):
    context = {}
    return render(request, 'poll/poll_vote.html', context)
