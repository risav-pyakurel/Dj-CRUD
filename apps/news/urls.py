from django.urls import path
from apps.news.views import *

app_name = 'news'

urlpatterns =[
    path('list/', NewsListView.as_view(), name= 'list'),
    path('create/', NewsCreateView.as_view(), name='create'),
    path('update/<int:pk>/', NewsUpdateView.as_view(), name = 'update'),
    path('delete/<int:pk>/',NewsDeleteView.as_view(), name='delete'),
]
