from django.contrib import admin

from .models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    model = BlogPost
    search_fields = ["author", "title", "content", "pub_date"]
    list_select_related = True


admin.site.register(BlogPost, BlogPostAdmin)
