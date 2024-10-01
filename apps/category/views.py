from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy

from apps.category.models import Category
from apps.category.forms import CategoryForm
from django.contrib import messages

class CategoryListView(LoginRequiredMixin, PermissionRequiredMixin,ListView):
    template_name = 'category/list.html'
    model = Category
    context_object_name ='categories'
    permission_required = 'category.view_required'
    login_url = 'accounts:login'
    raise_exception = 'True'


class CategoryCreateView(LoginRequiredMixin, PermissionRequiredMixin,CreateView):
    model = Category
    template_name = 'category/form.html'
    form_class = CategoryForm
    success_url = reverse_lazy('category:create')
    permission_required ='category.add_category'
    login_url = 'accounts:login'
    raise_exception = 'True'


class CategoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin,UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/form.html'
    success_url = reverse_lazy('category:list')
    permission_required = 'category.change_category'
    login_url = 'accounts:login'
    raise_exception = True




class CategoryDeleteView(LoginRequiredMixin, PermissionRequiredMixin,DeleteView):
    model = Category
    template_name = None
    success_url = reverse_lazy('category:list')
    permission_required = 'category.delete_category'
    login_url = 'accounts:login'
    raise_exception = True
   