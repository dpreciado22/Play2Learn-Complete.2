from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect

from .models import GameScore, Review

class HomePageView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["featured_reviews"] = Review.objects.order_by("-id")[:10]
        ctx["top_math"] = (
            GameScore.objects.filter(game="math_facts")
            .order_by("-score", "-finished_at")[:10]
        )
        ctx["top_anagram"] = (
            GameScore.objects.filter(game="anagram_hunt")
            .order_by("-score", "-finished_at")[:10]
        )
        return ctx


class AboutUsView(TemplateView):
    template_name = "pages/about_us.html"


class MyAccountView(LoginRequiredMixin, TemplateView):
    template_name = "pages/my_account.html"
    login_url = "account_login"


class LeaderboardListView(ListView):
    model = GameScore


class GameScoreDetailView(DetailView):
    model = GameScore


class ReviewListView(ListView):
    model = Review


class ReviewDetailView(DetailView):
    model = Review


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ["title", "body"]
    login_url = "account_login"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class OwnerOrStaffMixin(UserPassesTestMixin):
    raise_exception = True  # show 403 instead of redirect
    def test_func(self):
        obj = self.get_object()
        u = self.request.user
        return u.is_authenticated and (u.is_staff or obj.user_id == u.id)


class ReviewUpdateView(LoginRequiredMixin, OwnerOrStaffMixin, UpdateView):
    model = Review
    fields = ["title", "body"]
    login_url = "account_login"


class ReviewDeleteView(LoginRequiredMixin, OwnerOrStaffMixin, DeleteView):
    model = Review
    success_url = reverse_lazy("pages:reviews")
    login_url = "account_login"


@login_required(login_url="account_login")
def record_math_score(request):
    if request.method == "POST":
        try:
            score_val = int(request.POST.get("score", 0))
        except (TypeError, ValueError):
            score_val = 0
        GameScore.objects.create(
            user=request.user,
            game="math_facts",
            score=score_val,
            settings={},
        )
    return redirect("pages:leaderboards")

class AboutUsView(TemplateView):
    template_name = "pages/about_us.html"

    def get(self, request, *args, **kwargs):
        messages.debug(request, 'Debug message.')
        messages.info(request, 'Info message.')
        messages.success(request, 'Success message.')
        messages.warning(request, 'Warning message.')
        messages.error(request, 'Error message.')
        return super().get(request, *args, **kwargs)