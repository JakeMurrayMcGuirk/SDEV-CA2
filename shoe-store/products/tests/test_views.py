from base64 import b64decode
from unittest.mock import patch

from django.test import TestCase, override_settings
from rest_framework.test import APIClient

from users.tests.factories import AdminUserFactory, UserFactory

from ..serializers import CategorySerializer, ProductModelSerializer
from .factories import CategoryFactory, ProductModelFactory

TEST_PNG = b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+ip1sAAAAASUVORK5CYII="
)


class TestCategory(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()
        self.admin = AdminUserFactory()
        self.instance = CategoryFactory()

    def test_anonymous_list_fails(self):
        """Test that anonymous users can't list Category instances"""

        resp = self.client.get("/api/v1/products/category/")
        self.assertEqual(resp.status_code, 403)

    def test_list(self):
        """Test that Category collection can be listed"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get("/api/v1/products/category/")
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_anonymous_get_fails(self):
        """Test that anonymous users can't retrieve Category instances"""

        resp = self.client.get(f"/api/v1/products/category/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_get(self):
        """Test that an instance of Category can be retrieved"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(f"/api/v1/products/category/{self.instance.id}/")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], self.instance.id)

    def test_anonymous_create_fails(self):
        """Test that anonymous users can't create a new Category"""

        resp = self.client.post("/api/v1/products/category/")
        self.assertEqual(resp.status_code, 403)

    @patch("products.views.CategoryViewSet.get_serializer")
    def test_create(self, mock_get_serializer):
        """Test create view for Category"""

        self.client.force_authenticate(user=self.user)
        serializer = mock_get_serializer.return_value
        serializer.is_valid.return_value = True
        serializer.data = CategorySerializer(self.instance).data

        resp = self.client.post("/api/v1/products/category/", {})
        self.assertEqual(resp.status_code, 201)

        mock_get_serializer.assert_called_once_with(data={})
        serializer.save.assert_called_once_with()

    def test_anonymous_update_fails(self):
        """Test that anonymous users can't update an existing Category"""

        resp = self.client.patch(f"/api/v1/products/category/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 403)

    def test_update(self):
        """Test Category update"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.patch(f"/api/v1/products/category/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 200)

    def test_anonymous_delete_fails(self):
        """Test that anonymous users can't delete Category"""

        resp = self.client.delete(f"/api/v1/products/category/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_delete(self):
        """Test Category deletion"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.delete(f"/api/v1/products/category/{self.instance.id}/")

        self.assertEqual(resp.status_code, 204)


class TestProductModel(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()
        self.admin = AdminUserFactory()
        self.instance = ProductModelFactory()

    def test_anonymous_list_fails(self):
        """Test that anonymous users can't list ProductModel instances"""

        resp = self.client.get("/api/v1/products/product-model/")
        self.assertEqual(resp.status_code, 403)

    def test_list(self):
        """Test that ProductModel collection can be listed"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get("/api/v1/products/product-model/")
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_anonymous_get_fails(self):
        """Test that anonymous users can't retrieve ProductModel instances"""

        resp = self.client.get(f"/api/v1/products/product-model/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_get(self):
        """Test that an instance of ProductModel can be retrieved"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(f"/api/v1/products/product-model/{self.instance.id}/")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], self.instance.id)

    def test_anonymous_create_fails(self):
        """Test that anonymous users can't create a new ProductModel"""

        resp = self.client.post("/api/v1/products/product-model/")
        self.assertEqual(resp.status_code, 403)

    @patch("products.views.ProductModelViewSet.get_serializer")
    def test_create(self, mock_get_serializer):
        """Test create view for ProductModel"""

        self.client.force_authenticate(user=self.user)
        serializer = mock_get_serializer.return_value
        serializer.is_valid.return_value = True
        serializer.data = ProductModelSerializer(self.instance).data

        resp = self.client.post("/api/v1/products/product-model/", {})
        self.assertEqual(resp.status_code, 201)

        mock_get_serializer.assert_called_once_with(data={})
        serializer.save.assert_called_once_with()

    def test_anonymous_update_fails(self):
        """Test that anonymous users can't update an existing ProductModel"""

        resp = self.client.patch(
            f"/api/v1/products/product-model/{self.instance.id}/", {}
        )
        self.assertEqual(resp.status_code, 403)

    def test_update(self):
        """Test ProductModel update"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.patch(
            f"/api/v1/products/product-model/{self.instance.id}/", {}
        )
        self.assertEqual(resp.status_code, 200)

    def test_anonymous_delete_fails(self):
        """Test that anonymous users can't delete ProductModel"""

        resp = self.client.delete(f"/api/v1/products/product-model/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_delete(self):
        """Test ProductModel deletion"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.delete(f"/api/v1/products/product-model/{self.instance.id}/")

        self.assertEqual(resp.status_code, 204)

    @patch("django.core.files.storage.FileSystemStorage.save")
    def test_upload_images(self, mock_save):
        """Test uploading ProductModel.images"""

        self.client.force_authenticate(user=self.admin)
        mock_save.return_value = "images/test.png"

        with override_settings(
            DEFAULT_FILE_STORAGE="django.core.files.storage.FileSystemStorage"
        ):
            resp = self.client.put(
                f"/api/v1/products/product-model/{self.instance.id}/upload_images/",
                TEST_PNG,
                content_type="image/png",
                HTTP_CONTENT_DISPOSITION='attachment; filename="test.png"',
            )
        self.assertEqual(resp.status_code, 204)
        mock_save.assert_called_once()
