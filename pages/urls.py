from django.urls import path
from . import views

app_name = "pages"

urlpatterns = [
    # Core pages
    path("", views.HomePageView.as_view(), name="homepage"),
    path("about-us/", views.AboutUsView.as_view(), name="about-us"),
    path("contact/", views.ContactView.as_view(), name="contact"),

    # Leaderboards
    path("leaderboards/", views.LeaderboardListView.as_view(), name="leaderboards"),
    path("leaderboards/score/<int:pk>/", views.GameScoreDetailView.as_view(), name="score-detail"),

    # Reviews
    path("reviews/", views.ReviewListView.as_view(), name="reviews"),
    path("reviews/create/", views.ReviewCreateView.as_view(), name="review-create"),
    path("reviews/<slug:slug>/", views.ReviewDetailView.as_view(), name="review-detail"),
    path("reviews/<slug:slug>/update/", views.ReviewUpdateView.as_view(), name="review-update"),
    path("reviews/<slug:slug>/delete/", views.ReviewDeleteView.as_view(), name="review-delete"),

    # Scores (AJAX from Vue apps)
    path("scores/math/record/", views.record_math_score, name="record-math-score"),
    path("scores/anagram/record/", views.record_anagram_score, name="record-anagram-score"),
]
