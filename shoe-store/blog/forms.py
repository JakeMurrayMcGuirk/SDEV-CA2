from django import forms
from .models import BlogPost



class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['author','title', 'content', 'pub_date']  # Add or remove fields as needed
