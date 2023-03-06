from django import forms
from news.models import Category


class NewsForm(forms.Form):
    title = forms.CharField(max_length=150, label='Title',
                            widget=forms.TextInput(attrs={'class': 'form-control'})
                            )
    content = forms.CharField(label='Text', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    is_published = forms.BooleanField(label='Published', initial=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      empty_label='Choose category',
                                      label='Category',
                                      widget=forms.Select(attrs={'class': 'form-control'})
                                      )
