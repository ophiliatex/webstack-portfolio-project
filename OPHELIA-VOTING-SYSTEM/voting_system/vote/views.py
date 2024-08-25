from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Candidate, Vote, Voter
from .forms import VoteForm
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def cast_vote(request):
    if request.method == 'POST':
        voter_id = request.POST.get('voter_id')
        candidate_id = request.POST.get('candidate_id')
        
        # Fetch the Voter and Candidate objects
        voter = get_object_or_404(Voter, id=voter_id)
        candidate = get_object_or_404(Candidate, id=candidate_id)

        # Create a Vote object
        Vote.objects.create(voter=voter, candidate=candidate)

        # Redirect to a success page
        return redirect('vote_success')

    # For GET requests, render the voting form template
    return render(request, 'vote/vote_form.html')
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