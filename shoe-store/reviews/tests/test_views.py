from unittest.mock import patch

from django.test import TestCase
from rest_framework.test import APIClient

from users.tests.factories import AdminUserFactory, UserFactory

from ..serializers import ProductReviewSerializer
from .factories import ProductReviewFactory


class TestProductReview(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()
        self.instance = ProductReviewFactory(user=self.user)

    def test_anonymous_list_fails(self):
        """Test that anonymous users can't list ProductReview instances"""

        resp = self.client.get("/api/v1/reviews/product-review/")
        self.assertEqual(resp.status_code, 403)

    def test_list(self):
        """Test that ProductReview collection can be listed"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get("/api/v1/reviews/product-review/")
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_anonymous_get_fails(self):
        """Test that anonymous users can't retrieve ProductReview instances"""

        resp = self.client.get(f"/api/v1/reviews/product-review/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_get(self):
        """Test that an instance of ProductReview can be retrieved"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(f"/api/v1/reviews/product-review/{self.instance.id}/")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], self.instance.id)

    def test_anonymous_create_fails(self):
        """Test that anonymous users can't create a new ProductReview"""

        resp = self.client.post("/api/v1/reviews/product-review/")
        self.assertEqual(resp.status_code, 403)

    @patch("reviews.views.ProductReviewViewSet.get_serializer")
    def test_create(self, mock_get_serializer):
        """Test create view for ProductReview"""

        self.client.force_authenticate(user=self.user)
        serializer = mock_get_serializer.return_value
        serializer.is_valid.return_value = True
        serializer.data = ProductReviewSerializer(self.instance).data

        resp = self.client.post("/api/v1/reviews/product-review/", {})
        self.assertEqual(resp.status_code, 201)

        mock_get_serializer.assert_called_once_with(data={})
        serializer.save.assert_called_once_with(user=self.user)

    def test_anonymous_update_fails(self):
        """Test that anonymous users can't update an existing ProductReview"""

        resp = self.client.patch(
            f"/api/v1/reviews/product-review/{self.instance.id}/", {}
        )
        self.assertEqual(resp.status_code, 403)

    def test_update(self):
        """Test ProductReview update"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.patch(
            f"/api/v1/reviews/product-review/{self.instance.id}/", {}
        )
        self.assertEqual(resp.status_code, 200)

    def test_anonymous_delete_fails(self):
        """Test that anonymous users can't delete ProductReview"""

        resp = self.client.delete(f"/api/v1/reviews/product-review/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_delete(self):
        """Test ProductReview deletion"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.delete(f"/api/v1/reviews/product-review/{self.instance.id}/")

        self.assertEqual(resp.status_code, 204)
