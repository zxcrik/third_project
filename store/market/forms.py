from django import forms
from .models import Category

class AddProductForm(forms.Form):
    name = forms.CharField(max_length=255)
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols':5}))
    price = forms.FloatField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())