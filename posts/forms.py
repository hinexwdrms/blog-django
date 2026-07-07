from django import forms          
from .models import Post          # import our Post model

class PostForm(forms.ModelForm):  # ModelForm automatically builds a form from a model
    class Meta:                   # tells Django which model and fields to use
        model = Post              
        fields = ['title', 'content']  