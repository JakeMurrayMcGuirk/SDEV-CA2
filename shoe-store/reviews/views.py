from rest_framework import viewsets

from . import permissions
from .models import ProductReview
from .serializers import ProductReviewSerializer
from django.views.generic.edit import CreateView
from .models import ProductReview


class ProductReviewViewSet(viewsets.ModelViewSet):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer
    permission_classes = (permissions.ProductReviewPermission,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ReviewCreateView(CreateView):
    model = ProductReview
    template_name = 'create_review.html'
    fields = ['product', 'user', 'rating', 'review_text']