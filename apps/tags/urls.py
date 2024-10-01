from django.urls import path

from apps.tags.views import TagListView, TagCreateView, TagUpdateView,TagDeleteView

app_name ='tags'

urlpatterns = [
    path('',TagListView.as_view(), name='list'),
    path('create/',TagCreateView.as_view(), name='create'),
    path('update/<int:pk>/',TagUpdateView.as_view(), name = 'update'),
    path('delete/<int:pk>', TagDeleteView.as_view(), name = 'delete'),
]
