from django.urls import path
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
    path("reviews/<int:pk>/", ReviewDetailView.as_view(), name="review-detail"),
    path("reviews/<int:pk>/update/", ReviewUpdateView.as_view(), name="review-update"),
    path("reviews/<int:pk>/delete/", ReviewDeleteView.as_view(), name="review-delete"),
]