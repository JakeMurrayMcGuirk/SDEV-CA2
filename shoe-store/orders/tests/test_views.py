from unittest.mock import patch

from django.test import TestCase
from rest_framework.test import APIClient

from users.tests.factories import AdminUserFactory, UserFactory

from ..serializers import OderitemSerializer, OrderSerializer
from .factories import OderitemFactory, OrderFactory


class TestOderitem(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()
        self.admin = AdminUserFactory()
        self.instance = OderitemFactory()

    def test_anonymous_list_fails(self):
        """Test that anonymous users can't list Oderitem instances"""

        resp = self.client.get("/api/v1/orders/oderitem/")
        self.assertEqual(resp.status_code, 403)

    def test_list(self):
        """Test that Oderitem collection can be listed"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get("/api/v1/orders/oderitem/")
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_anonymous_get_fails(self):
        """Test that anonymous users can't retrieve Oderitem instances"""

        resp = self.client.get(f"/api/v1/orders/oderitem/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_get(self):
        """Test that an instance of Oderitem can be retrieved"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(f"/api/v1/orders/oderitem/{self.instance.id}/")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], self.instance.id)

    def test_anonymous_create_fails(self):
        """Test that anonymous users can't create a new Oderitem"""

        resp = self.client.post("/api/v1/orders/oderitem/")
        self.assertEqual(resp.status_code, 403)

    @patch("orders.views.OderitemViewSet.get_serializer")
    def test_create(self, mock_get_serializer):
        """Test create view for Oderitem"""

        self.client.force_authenticate(user=self.user)
        serializer = mock_get_serializer.return_value
        serializer.is_valid.return_value = True
        serializer.data = OderitemSerializer(self.instance).data

        resp = self.client.post("/api/v1/orders/oderitem/", {})
        self.assertEqual(resp.status_code, 201)

        mock_get_serializer.assert_called_once_with(data={})
        serializer.save.assert_called_once_with()

    def test_anonymous_update_fails(self):
        """Test that anonymous users can't update an existing Oderitem"""

        resp = self.client.patch(f"/api/v1/orders/oderitem/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 403)

    def test_update(self):
        """Test Oderitem update"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.patch(f"/api/v1/orders/oderitem/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 200)

    def test_anonymous_delete_fails(self):
        """Test that anonymous users can't delete Oderitem"""

        resp = self.client.delete(f"/api/v1/orders/oderitem/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_delete(self):
        """Test Oderitem deletion"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.delete(f"/api/v1/orders/oderitem/{self.instance.id}/")

        self.assertEqual(resp.status_code, 204)


class TestOrder(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()
        self.instance = OrderFactory(user=self.user)

    def test_anonymous_list_fails(self):
        """Test that anonymous users can't list Order instances"""

        resp = self.client.get("/api/v1/orders/order/")
        self.assertEqual(resp.status_code, 403)

    def test_list(self):
        """Test that Order collection can be listed"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get("/api/v1/orders/order/")
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_anonymous_get_fails(self):
        """Test that anonymous users can't retrieve Order instances"""

        resp = self.client.get(f"/api/v1/orders/order/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_get(self):
        """Test that an instance of Order can be retrieved"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.get(f"/api/v1/orders/order/{self.instance.id}/")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], self.instance.id)

    def test_anonymous_create_fails(self):
        """Test that anonymous users can't create a new Order"""

        resp = self.client.post("/api/v1/orders/order/")
        self.assertEqual(resp.status_code, 403)

    @patch("orders.views.OrderViewSet.get_serializer")
    def test_create(self, mock_get_serializer):
        """Test create view for Order"""

        self.client.force_authenticate(user=self.user)
        serializer = mock_get_serializer.return_value
        serializer.is_valid.return_value = True
        serializer.data = OrderSerializer(self.instance).data

        resp = self.client.post("/api/v1/orders/order/", {})
        self.assertEqual(resp.status_code, 201)

        mock_get_serializer.assert_called_once_with(data={})
        serializer.save.assert_called_once_with(user=self.user)

    def test_anonymous_update_fails(self):
        """Test that anonymous users can't update an existing Order"""

        resp = self.client.patch(f"/api/v1/orders/order/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 403)

    def test_update(self):
        """Test Order update"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.patch(f"/api/v1/orders/order/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 200)

    def test_anonymous_delete_fails(self):
        """Test that anonymous users can't delete Order"""

        resp = self.client.delete(f"/api/v1/orders/order/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_delete(self):
        """Test Order deletion"""

        self.client.force_authenticate(user=self.user)
        resp = self.client.delete(f"/api/v1/orders/order/{self.instance.id}/")

        self.assertEqual(resp.status_code, 204)
