from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Voter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_eligible = models.BooleanField(default=True)
    has_voted = models.BooleanField(default=False)
    
class Candidate(models.Model):
    name = models.CharField(max_length=100)
    party = models.CharField(max_length=100)
    manifesto = models.TextField()
    
class Candidate(models.Model):
    name = models.CharField(max_length=100)
    party = models.CharField(max_length=100)
    manifesto = models.TextField()
   

class Vote(models.Model):
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
  