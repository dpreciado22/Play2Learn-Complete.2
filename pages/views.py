import json
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse, HttpResponseBadRequest
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.core.mail import mail_admins
from .forms import ContactForm
from .models import GameScore, Review

GAME_MATH = "math-facts"
GAME_ANAGRAM = "anagram-hunt"


class HomePageView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx["featured_reviews"] = Review.objects.order_by("-id")[:10]

        ctx["top_math"] = (
            GameScore.objects.filter(game=GAME_MATH)
            .select_related("user")
            .order_by("-score", "-finished_at")[:10]
        )
        ctx["top_anagram"] = (
            GameScore.objects.filter(game=GAME_ANAGRAM)
            .select_related("user")
            .order_by("-score", "-finished_at")[:10]
        )

        if self.request.user.is_authenticated:
            u = self.request.user
            ctx["my_recent_scores"] = (
                GameScore.objects.filter(user=u)
                .order_by("-finished_at")[:10]
            )
        return ctx
    
class LeaderboardListView(TemplateView):
    template_name = "pages/leaderboards.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["math_top"] = (
            GameScore.objects.filter(game=GAME_MATH)
            .select_related("user")
            .order_by("-score", "-finished_at")
        )
        ctx["anagram_top"] = (
            GameScore.objects.filter(game=GAME_ANAGRAM)
            .select_related("user")
            .order_by("-score", "-finished_at")
        )
        if self.request.user.is_authenticated:
            u = self.request.user
            ctx["my_math"] = (
                GameScore.objects.filter(user=u, game=GAME_MATH)
                .order_by("-finished_at")
            )
            ctx["my_anagram"] = (
                GameScore.objects.filter(user=u, game=GAME_ANAGRAM)
                .order_by("-finished_at")
            )
        return ctx


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

class AboutUsView(TemplateView):
    template_name = "pages/about_us.html"

    def get(self, request, *args, **kwargs):
        messages.info(request, "Welcome to Play2Learn!")
        return super().get(request, *args, **kwargs)

class ContactView(FormView):
    template_name = "pages/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("pages:contact")

    def form_valid(self, form):
        data = form.cleaned_data
        subject = f"Contact message from {data['name']} <{data['email']}>"
        body = data["message"]
        
        mail_admins(subject, body, fail_silently=False)
        messages.success(self.request, "Thanks! Your message has been sent.")
        return super().form_valid(form)


@login_required
@require_POST
def record_math_score(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
        score = int(data.get("score", 0))
    except (ValueError, json.JSONDecodeError):
        return HttpResponseBadRequest("Invalid payload")

    gs = GameScore.objects.create(
        user=request.user, game=GAME_MATH, score=max(score, 0)
    )
    return JsonResponse({"ok": True, "id": gs.pk, "score": gs.score}, status=201)

@login_required
@require_POST
def record_anagram_score(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
        score = int(data.get("score", 0))
    except (ValueError, json.JSONDecodeError):
        return HttpResponseBadRequest("Invalid payload")

    gs = GameScore.objects.create(
        user=request.user, game=GAME_ANAGRAM, score=max(score, 0)
    )
    return JsonResponse({"ok": True, "id": gs.pk, "score": gs.score}, status=201)
