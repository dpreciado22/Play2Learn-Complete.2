import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse, HttpResponseBadRequest
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import (
    TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
)

from .models import GameScore, Review


class HomePageView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["featured_reviews"] = Review.objects.order_by("-id")[:10]

        ctx["top_math"] = (
            GameScore.objects
            .filter(game="math-facts")
            .select_related("user")
            .order_by("-score", "-created")[:10]
        )
        ctx["top_anagram"] = (
            GameScore.objects
            .filter(game="anagram-hunt")
            .select_related("user")
            .order_by("-score", "-created")[:10]
        )

        if self.request.user.is_authenticated:
            u = self.request.user
            ctx["my_recent_scores"] = (
                GameScore.objects
                .filter(user=u)
                .select_related("user")
                .order_by("-created")[:10]
            )
        return ctx


class AboutUsView(TemplateView):
    template_name = "pages/about_us.html"

    def get(self, request, *args, **kwargs):
        messages.success(request, "Welcome to Play2Learn!")
        return super().get(request, *args, **kwargs)


class LeaderboardListView(ListView):
    model = GameScore
    template_name = "pages/leaderboards.html"
    context_object_name = "scores"

    def get_queryset(self):
        return (
            GameScore.objects
            .select_related("user")
            .order_by("-score", "-created")[:200]
        )


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
    raise_exception = True

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


@login_required
@require_POST
def record_math_score(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
        score = int(data.get("score", 0))
    except (ValueError, json.JSONDecodeError):
        return HttpResponseBadRequest("Invalid payload")

    score = max(0, score)
    gs = GameScore.objects.create(user=request.user, game="math-facts", score=score)
    return JsonResponse({"ok": True, "id": gs.pk, "score": gs.score})


@login_required
@require_POST
def record_anagram_score(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
        score = int(data.get("score", 0))
    except (ValueError, json.JSONDecodeError):
        return HttpResponseBadRequest("Invalid payload")

    score = max(0, score)
    gs = GameScore.objects.create(user=request.user, game="anagram-hunt", score=score)
    return JsonResponse({"ok": True, "id": gs.pk, "score": gs.score})
