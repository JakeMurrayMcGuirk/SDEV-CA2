from rest_framework import viewsets

from . import permissions
from .models import ProductReview
from .serializers import ProductReviewSerializer


class ProductReviewViewSet(viewsets.ModelViewSet):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer
    permission_classes = (permissions.ProductReviewPermission,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
