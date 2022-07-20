from django.shortcuts import render

# Poll views

def home(request):
    context = {}
    return render(request, 'poll/poll_home.html', context)

def create(request):
    context = {}
    return render(request, 'poll/poll_create.html', context)

def results(request):
    context = {}
    return render(request, 'poll/poll_results.html', context)

def vote(request):
    context = {}
    return render(request, 'poll/poll_vote.html', context)
