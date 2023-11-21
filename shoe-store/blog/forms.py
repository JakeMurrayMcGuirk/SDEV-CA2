from django import forms
from .models import BlogPost



class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'pub_date', 'image']  # Add or remove fields as needed
