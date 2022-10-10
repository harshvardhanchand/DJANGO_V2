from django import forms
from .models import Review
from django.forms import ModelForm


class ReviewForm(forms.Form):
    first_name = forms.CharField(max_length=50, label='First Name')
    last_name = forms.CharField(max_length=50, label='Last Name')
    email = forms.EmailField(max_length=50, label='Email')
    review = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'myform'}), label='Review')


class reviewForm(ModelForm):
    class Meta:
        model = Review
