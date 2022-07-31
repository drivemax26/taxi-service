from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from taxi.models import Manufacturer

MANUFACTURER_URL = reverse("taxi:manufacturer-list")


class PublicManufacturerTest(TestCase):

    def test_login_required(self):
        res = self.client.get(MANUFACTURER_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateManufacturerTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            "test",
            "password123"
        )
        self.client.force_login(self.user)

    def test_retrieve_manufacturer(self):
        Manufacturer.objects.create(name="Tesla", country="USA")
        Manufacturer.objects.create(name="Honda", country="Canada")

        res = self.client.get(MANUFACTURER_URL)

        manufacturer = Manufacturer.objects.all()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(list(res.context["manufacturer_list"]), list(manufacturer))

        self.assertTemplateUsed(res, "taxi/manufacturer_list.html")
