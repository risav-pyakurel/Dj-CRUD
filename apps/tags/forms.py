from django import forms
from apps.tags.models import Tag


class TagForm(forms.ModelForm):
    name = forms.CharField( max_length= 50, required=True)
    description = forms.CharField(max_length=200)

    class Meta:
        model = Tag
        fields = ['name', 'description']
