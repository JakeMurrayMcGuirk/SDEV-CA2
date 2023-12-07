from unittest.mock import patch

from django.test import TestCase
from rest_framework.test import APIClient

from users.tests.factories import AdminUserFactory, UserFactory

from ..serializers import CartItemSerializer, CartSerializer
from .factories import CartFactory, CartItemFactory


class TestCart(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()
        self.instance = CartFactory(user=self.user)

    def test_anonymous_list_fails(self):
        """Test that anonymous users can't list Cart instances"""

        resp = self.client.get("/api/v1/cart/cart/")
        self.assertEqual(resp.status_code, 403)

    def test_list(self):
        """Test that Cart collection can be listed"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get("/api/v1/cart/cart/")
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_anonymous_get_fails(self):
        """Test that anonymous users can't retrieve Cart instances"""

        resp = self.client.get(f"/api/v1/cart/cart/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_get(self):
        """Test that an instance of Cart can be retrieved"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(f"/api/v1/cart/cart/{self.instance.id}/")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], self.instance.id)

    def test_anonymous_create_fails(self):
        """Test that anonymous users can't create a new Cart"""

        resp = self.client.post("/api/v1/cart/cart/")
        self.assertEqual(resp.status_code, 403)

    @patch("cart.views.CartViewSet.get_serializer")
    def test_create(self, mock_get_serializer):
        """Test create view for Cart"""

        self.client.force_authenticate(user=self.user)
        serializer = mock_get_serializer.return_value
        serializer.is_valid.return_value = True
        serializer.data = CartSerializer(self.instance).data

        resp = self.client.post("/api/v1/cart/cart/", {})
        self.assertEqual(resp.status_code, 201)

        mock_get_serializer.assert_called_once_with(data={})
        serializer.save.assert_called_once_with(user=self.user)

    def test_anonymous_update_fails(self):
        """Test that anonymous users can't update an existing Cart"""

        resp = self.client.patch(f"/api/v1/cart/cart/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 403)

    def test_update(self):
        """Test Cart update"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.patch(f"/api/v1/cart/cart/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 200)

    def test_anonymous_delete_fails(self):
        """Test that anonymous users can't delete Cart"""

        resp = self.client.delete(f"/api/v1/cart/cart/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_delete(self):
        """Test Cart deletion"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.delete(f"/api/v1/cart/cart/{self.instance.id}/")

        self.assertEqual(resp.status_code, 204)


class TestCartItem(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()
        self.admin = AdminUserFactory()
        self.instance = CartItemFactory()

    def test_anonymous_list_fails(self):
        """Test that anonymous users can't list CartItem instances"""

        resp = self.client.get("/api/v1/cart/cart-item/")
        self.assertEqual(resp.status_code, 403)

    def test_list(self):
        """Test that CartItem collection can be listed"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get("/api/v1/cart/cart-item/")
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_anonymous_get_fails(self):
        """Test that anonymous users can't retrieve CartItem instances"""

        resp = self.client.get(f"/api/v1/cart/cart-item/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_get(self):
        """Test that an instance of CartItem can be retrieved"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(f"/api/v1/cart/cart-item/{self.instance.id}/")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], self.instance.id)

    def test_anonymous_create_fails(self):
        """Test that anonymous users can't create a new CartItem"""

        resp = self.client.post("/api/v1/cart/cart-item/")
        self.assertEqual(resp.status_code, 403)

    @patch("cart.views.CartItemViewSet.get_serializer")
    def test_create(self, mock_get_serializer):
        """Test create view for CartItem"""

        self.client.force_authenticate(user=self.user)
        serializer = mock_get_serializer.return_value
        serializer.is_valid.return_value = True
        serializer.data = CartItemSerializer(self.instance).data

        resp = self.client.post("/api/v1/cart/cart-item/", {})
        self.assertEqual(resp.status_code, 201)

        mock_get_serializer.assert_called_once_with(data={})
        serializer.save.assert_called_once_with()

    def test_anonymous_update_fails(self):
        """Test that anonymous users can't update an existing CartItem"""

        resp = self.client.patch(f"/api/v1/cart/cart-item/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 403)

    def test_update(self):
        """Test CartItem update"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.patch(f"/api/v1/cart/cart-item/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 200)

    def test_anonymous_delete_fails(self):
        """Test that anonymous users can't delete CartItem"""

        resp = self.client.delete(f"/api/v1/cart/cart-item/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_delete(self):
        """Test CartItem deletion"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.delete(f"/api/v1/cart/cart-item/{self.instance.id}/")

        self.assertEqual(resp.status_code, 204)
