from django.urls import path
from django.views.generic import RedirectView
from . import views
urlpatterns = [
    path('', views.cast_vote, name='home'),  # Root URL (http://127.0.0.1:8000/vote/) for voting
    path('cast_vote/', views.cast_vote, name='cast_vote'),
    path('results/', views.view_results, name='view_results'),
    path('success/', views.vote_success, name='vote_success'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    
]
