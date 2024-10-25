"""
URL configuration for circl project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.auth import urls
from django.contrib.auth import views as auth_views
from dash import views as dash_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", RedirectView.as_view(url="/dash/contacts/", permanent=True)),  # Redirect root to /dash/
    path("dash/", include("dash.urls")),  # Include URLs from dash app
    path('accounts/', include(urls)),
    path('login/', auth_views.LoginView.as_view(template_name='dash/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', dash_views.signup, name='signup'),
]
    
