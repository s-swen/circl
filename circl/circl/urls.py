from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.auth import urls
from dash import views as dash_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", RedirectView.as_view(url="/dash/contacts/", permanent=True)),  # Redirect root to /dash/
    path("dash/", include("dash.urls")),  # Include URLs from dash app
    path('accounts/', include(urls)),
    path('login/', dash_views.login_view, name='login'),
    path('signup/', dash_views.signup_view, name='signup'),
]
    
