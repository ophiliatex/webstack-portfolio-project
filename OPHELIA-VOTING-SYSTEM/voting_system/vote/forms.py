from django import forms
from .models import Candidate

class VoteForm(forms.Form):
    candidate = forms.ModelChoiceField(
        queryset=Candidate.objects.all(),
        widget=forms.RadioSelect,
        empty_label=None,
        label="Select your candidate"
    )
