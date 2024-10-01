from django import forms

from apps.category.models import Category


class CategoryForm(forms.ModelForm):
    # name = forms.CharField(max_length=100)
    # description = forms.CharField(max_length=500)

    class Meta:
        model = Category
        fields = ['name', 'description']
