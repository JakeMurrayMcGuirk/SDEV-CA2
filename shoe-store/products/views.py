from rest_framework import decorators, parsers, response, status, viewsets

from . import permissions
from .models import Category, ProductModel
from .serializers import CategorySerializer, ProductModelSerializer


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
        """
        Upload images using a PUT request.

        Use the Content-Type header to specify the file type, and the
        Content-Disposition header to specify the filename, for example:

            Content-Type: image/png
            Content-Disposition: attachment; filename=screenshot.png
        """

        obj = self.get_object()
        file = request.data.get("file")
        if not file:
            return response.Response(
                {"error": "Missing content"},
                status=status.HTTP_404_BAD_REQUEST,
            )

        obj.images.save(file.name, file, save=True)
        return response.Response(status=status.HTTP_204_NO_CONTENT)
