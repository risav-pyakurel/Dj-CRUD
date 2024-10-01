from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models.query import QuerySet
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

from apps.tags.models import Tag
from apps.tags.forms import TagForm

class TagListView(LoginRequiredMixin, PermissionRequiredMixin,ListView):
    template_name= 'tags/list.html'
    context_object_name = 'tag_list'






class TagCreateView(LoginRequiredMixin, PermissionRequiredMixin,CreateView):
    model = Tag
    template_name = 'tags/form.html'
    context_object_name = 'tags'
    login_url ='accounts:login'
    raise_exception =True


class TagUpdateView(LoginRequiredMixin, PermissionRequiredMixin,UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "tags/form.html"
    success_url = reverse_lazy('tags:list')
    permission_required = 'tags.change_tag'
    login_url ='accounts:login'
    raise_exception =True




class TagDeleteView(LoginRequiredMixin, PermissionRequiredMixin,DeleteView):
    model = Tag
    template_name = None
    success_url = reverse_lazy('tag_list')
    permission_required = 'tags.delete_tag'
    login_url = 'accounts:login'
    raise_exception = True


