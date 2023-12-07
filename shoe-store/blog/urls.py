from rest_framework import routers
from django.urls import path, include
from .views import blog_list, blog_detail, blog_create, blog_delete
from . import views

from .views import BlogPostViewSet

blog_router = routers.SimpleRouter()
blog_router.register(r"blog/blog-post", BlogPostViewSet)


urlpatterns = [
    path('api/', include(blog_router.urls)),
    path('blog/delete/<int:blog_id>/', views.blog_delete, name='blog_delete'),
    path('blogs/', blog_list, name='blog_list'),  
    path('blogs/<int:blog_id>/', blog_detail, name='blog_detail'),  
    path('blogs/create/', blog_create, name='blog_create'),  
  
]
urlpatterns += blog_router.urls