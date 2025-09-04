from django.views.generic import TemplateView, ListView, DetailView
from .models import GameScore

class HomePageView(TemplateView):
    template_name = "pages/home.html"   

class AboutUsView(TemplateView):
    template_name = "pages/about_us.html"

class MyAccountView(TemplateView):  
    template_name = "pages/my_account.html"

class LeaderboardListView(ListView):
    model = GameScore

class GameScoreDetailView(DetailView):
    model = GameScore