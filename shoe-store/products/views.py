from rest_framework import decorators, parsers, response, status, viewsets
from django.shortcuts import render
from . import permissions
from .models import Category, ProductModel
from .serializers import CategorySerializer, ProductModelSerializer
from django.views.generic import ListView, DetailView


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.CategoryPermission,)


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer
    permission_classes = (permissions.ProductModelPermission,)

    @decorators.action(
        detail=True,
        methods=["put"],
        name="Upload images",
        parser_classes=[parsers.FileUploadParser],
    )
    def upload_images(self, request, pk=None):
        obj = self.get_object()
        file = request.data.get("file")
        if not file:
            return response.Response(
                {"error": "Missing content"},
                status=status.HTTP_404_BAD_REQUEST,
            )

        obj.images.save(file.name, file, save=True)
        return response.Response(status=status.HTTP_204_NO_CONTENT)


class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'


class ProductListView(ListView):
    model = ProductModel
    template_name = 'product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        if 'pk' in self.kwargs:  # If a category is specified
            return ProductModel.objects.filter(category__id=self.kwargs['pk'])
        else:  # If no category is specified, show all products
            return ProductModel.objects.all()
        


def product_list(request):
    products = ProductModel.objects.all()  # Fetch all products
    return render(request, 'product_list.html', {'products': products})

class AllProductListView(ListView):
    model = ProductModel
    template_name = 'product_list.html'  # Template to render the product list
    context_object_name = 'products'

    def get_queryset(self):
        return ProductModel.objects.all()
    
class ProductDetailView(DetailView):
    model = ProductModel
    template_name = 'product_detail.html'
    context_object_name = 'product'