from django.urls import path
from .views import HomePageView, AboutUsView, MyAccountView

app_name = "pages"

urlpatterns = [
    path("", HomePageView.as_view(), name="homepage"),
    path("about-us/", AboutUsView.as_view(), name="about-us"),
    path("account/", MyAccountView.as_view(), name="my-account"),
]