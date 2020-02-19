"""nba_schedule URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import include, url
from mainapp import views as mainapp_views
from users import views as user_views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='mainapp/index.html')),
    url(r'^upload/', mainapp_views.upload_page, name='upload'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    url(r'^profile/', user_views.profile, name='profile'),
    url(r'^contact/', user_views.contact, name='contact'),
    url(r'^legalmentions/', user_views.mentions, name='mentions'),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
