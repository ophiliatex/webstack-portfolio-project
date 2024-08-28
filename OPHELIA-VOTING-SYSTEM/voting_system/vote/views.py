from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Candidate, Vote, Voter
from .forms import VoteForm
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
# Create your views here.
@login_required
def cast_vote(request):
    if request.method == 'POST':
        voter_id = request.POST.get('voter_id')
        candidate_id = request.POST.get('candidate_id')

        try:
            voter = Voter.objects.get(id=voter_id)
            candidate = Candidate.objects.get(id=candidate_id)
        except Voter.DoesNotExist:
            return HttpResponse("Voter not found.", status=404)
        except Candidate.DoesNotExist:
            return HttpResponse("Candidate not found.", status=404)

        # If both objects are found, create the vote
        Vote.objects.create(voter=voter, candidate=candidate)

        # Redirect to a success page
        return redirect('vote_success')

    # For GET requests, render the voting form template
    return render(request, 'registration/login.html')

@login_required
def view_results(request):
    candidates = Candidate.objects.all()
    results = {candidate: Vote.objects.filter(candidate=candidate).count() for candidate in candidates}
    return render(request, 'vote/results.html', {'results': results})

def vote_success(request):
    return render(request, 'vote/vote_success.html')
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after signup
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
@login_required
def profile(request):
    return render(request, 'registration/profile.html')
