from django import forms
from django.contrib.auth.models import User
from .models import *

class PostForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':2, 'placeholder': '¿Que paso?'}), required=True)

    class Meta:
        model = Post
        fields = ['content']