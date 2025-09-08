from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin
    path("admin/doc/", include("django.contrib.admindocs.urls")),
    path("admin/", admin.site.urls),

    # Users app Auth
    path('', include('users.urls')),
    path('account/', include('allauth.urls')),

    # Local Apps
    path("", include("pages.urls")),
    path("", include(("games.urls","games"), namespace="games")),

]
