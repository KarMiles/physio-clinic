from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse

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


def poll_results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    context = {
        'poll': poll
    }
    return render(request, 'poll/poll_results.html', context)
