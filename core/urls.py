"""
URL configuration for core project.

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
from django.urls import path, include, reverse_lazy
from django.views.generic import RedirectView
from apps.category import urls
from apps.tags import urls
from apps.accounts import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('apps.accounts.urls', namespace= 'accounts')),
    path('category/', include('apps.category.urls', namespace= 'category')),
    path('tags/', include('apps.tags.urls', namespace='news')),
    path('news/', include('apps.news.urls', namespace = 'tags')),
   path('', RedirectView.as_view(url=reverse_lazy('accounts:login'), permanent = False), name = 'home'),
]
