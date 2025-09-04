from django.urls import path
from .views import (
    HomePageView, AboutUsView, MyAccountView, LeaderboardListView, GameScoreDetailView,
)

app_name = "pages"

urlpatterns = [
    path("", HomePageView.as_view(), name="homepage"),
    path("about-us/", AboutUsView.as_view(), name="about-us"),
    path("leaderboards/", LeaderboardListView.as_view(), name="leaderboards"),
    path("my-account/", MyAccountView.as_view(), name="my-account"),
    path("leaderboards/score/<int:pk>/", GameScoreDetailView.as_view(), name="score-detail"),
]