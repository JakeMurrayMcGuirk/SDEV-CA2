from rest_framework import viewsets

from . import permissions
from .models import BlogPost
from .serializers import BlogPostSerializer


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = (permissions.BlogPostPermission,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
