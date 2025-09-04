from django.urls import reverse_lazy 
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import GameScore, Review

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

class ReviewListView(ListView):
    model = Review 

class ReviewDetailView(DetailView):
    model = Review 

class ReviewCreateView(CreateView):
    model = Review
    fields = ['title', 'body'] 

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        else:
            form.instance.user = User.objects.first()
        return super().form_valid(form)

class ReviewUpdateView(UpdateView):
    model = Review
    fields = ['title', 'body']

class ReviewDeleteView(DeleteView):
    model = Review
    success_url = reverse_lazy('pages:reviews')