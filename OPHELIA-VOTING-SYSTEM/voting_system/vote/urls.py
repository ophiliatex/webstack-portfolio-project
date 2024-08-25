from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='vote/', permanent=False), name='home'),  # Redirect root URL to /vote/
    path('vote/', views.cast_vote, name='cast_vote'),
    path('results/', views.view_results, name='view_results'),
    path('success/', views.vote_success, name='vote_success'),
]
