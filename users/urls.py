from django.urls import path
from .views import MyAccountPageView, CustomPasswordChangeView

app_name = "users"

urlpatterns = [
    path('my-account/', MyAccountPageView.as_view(), name='my-account'),
    path('password/change/', CustomPasswordChangeView.as_view(),
         name='password_change'),
]
