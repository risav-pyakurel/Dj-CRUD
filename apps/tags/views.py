from django.db.models.query import QuerySet
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

from apps.tags.models import Tag
from apps.tags.forms import TagForm

class TagListView(ListView):
    template_name= 'tags/list.html'
    context_object_name = 'tag_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Tag'
        return context

    def get_queryset(self):
        queryset = Tag.objects.all()
        return queryset



class TagCreateView(CreateView):
    model = Tag
    template_name = 'tags/form.html'
    form_class = TagForm
    success_url = reverse_lazy('tag_list')

    def form_valid(self, form):
        return super().form_valid(form)

class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "tags/form.html"
    success_url = reverse_lazy('tag_list')

    def form_valid(self, form):
        return super().form_valid(form)


class TagDeleteView(DeleteView):
    model = Tag
    template_name = None
    success_url = reverse_lazy('tag_list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
