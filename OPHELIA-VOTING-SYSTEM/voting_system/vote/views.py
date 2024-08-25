from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Candidate, Vote, Voter
from .forms import VoteForm

# Create your views here.

@login_required
def cast_vote(request):
    voter = Voter.objects.get(user=request.user)
    if voter.has_voted:
        return render(request, 'vote/already_voted.html')

    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            vote = Vote(voter=voter, candidate=form.cleaned_data['candidate'])
            vote.save()
            voter.has_voted = True
            voter.save()
            return redirect('vote_success')
    else:
        form = VoteForm()

    return render(request, 'vote/cast_vote.html', {'form': form})

@login_required
def view_results(request):
    candidates = Candidate.objects.all()
    results = {candidate: Vote.objects.filter(candidate=candidate).count() for candidate in candidates}
    return render(request, 'vote/results.html', {'results': results})

def vote_success(request):
    return render(request, 'vote/vote_success.html')