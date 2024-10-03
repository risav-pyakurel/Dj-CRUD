from django.urls import path
from django.contrib.auth import views as auth_views
from apps.accounts import views


app_name = 'accounts'

urlpatterns = [
    path('login/',views.UserLoginView.as_view(), name= 'login'),
   
]
