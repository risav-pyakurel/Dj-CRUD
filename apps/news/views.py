from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from apps.news.models import News
from apps.news.forms import NewsForm

class NewsListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    template_name = 'news/list.html'
    model = News
    context_object_name = 'name'
    permission_required = 'news.views_news'
    login_url = 'accounts:login'
    raise_exception = True


class NewsCreateView(LoginRequiredMixin, PermissionRequiredMixin,CreateView):
    model = News
    template_name = 'news/form.html'
    form_class = NewsForm
    success_url = reverse_lazy('news:list')
    permission_required= 'news.add_news'
    login_url = 'accounts:login'
    raise_exception = True


class NewsUpdateView(LoginRequiredMixin, PermissionRequiredMixin,UpdateView):
    model = News
    template_name = 'news/form.html'
    form_class = NewsForm
    success_url= reverse_lazy('news_list')
    permission_required= 'news.delete_news'
    login_url = 'accounts:login'
    raise_exception = True


class NewsDeleteView(LoginRequiredMixin, PermissionRequiredMixin,DeleteView):
    model = News
    success_url = reverse_lazy('news_list')
    permission_required= 'news.delete_news'
    login_url = 'accounts:login'
    raise_exception = True
