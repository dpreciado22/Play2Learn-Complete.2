from django.urls import path
from .views import MyAccountPageView, CustomPasswordChangeView

urlpatterns = [
    path('my-account/', MyAccountPageView.as_view(), name='my-account'),
    path('password/change/', CustomPasswordChangeView.as_view(),
         name='account_change_password'),
]
