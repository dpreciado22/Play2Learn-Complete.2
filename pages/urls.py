from django.urls import path
from . import views
from .views import (
    HomePageView, AboutUsView, MyAccountView, LeaderboardListView, GameScoreDetailView, ReviewListView, ReviewDetailView, ReviewCreateView, ReviewUpdateView, ReviewDeleteView,
)

app_name = "pages"

urlpatterns = [
    path("", HomePageView.as_view(), name="homepage"),
    path("about-us/", AboutUsView.as_view(), name="about-us"),
    path("my-account/", MyAccountView.as_view(), name="my-account"),

    # Leaderboards
    path("leaderboards/", LeaderboardListView.as_view(), name="leaderboards"),
    path("leaderboards/score/<int:pk>/", GameScoreDetailView.as_view(), name="score-detail"),

    # Reviews
    path("reviews/", ReviewListView.as_view(), name="reviews"),
    path("reviews/create/", ReviewCreateView.as_view(), name="review-create"),
    path("reviews/<slug:slug>/", ReviewDetailView.as_view(), name="review-detail"),
    path("reviews/<slug:slug>/update/", ReviewUpdateView.as_view(), name="review-update"),
    path("reviews/<slug:slug>/delete/", ReviewDeleteView.as_view(), name="review-delete"),

    # Gamescore
    path('scores/math/record/', views.record_math_score, name='record-math-score'),
]