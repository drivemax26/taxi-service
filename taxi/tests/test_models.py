from django.contrib.auth import get_user_model
from django.test import TestCase

from taxi.models import Manufacturer, Car


class ModelsTest(TestCase):
    def test_manufacturer_str(self):
        manufacturer_ = Manufacturer.objects.create(
            name="test",
            country="test"
        )
        self.assertEqual(str(manufacturer_), f"{manufacturer_.name} {manufacturer_.country}")

    def test_driver_str(self):
        driver = get_user_model().objects.create_user(
            username="test",
            password="test1234",
            first_name="test first",
            last_name="test last"
        )

        self.assertEqual(str(driver), f"{driver.username} ({driver.first_name} {driver.last_name})")

    def test_car_str(self):
        manufacturer_ = Manufacturer.objects.create(
            name="test",
            country="test"
        )
        car = Car.objects.create(
            model="test",
            manufacturer=manufacturer_
        )

        self.assertEqual(str(car), car.model)

    def test_create_driver_with_license(self):
        username = "test",
        first_name = "test first",
        last_name = "test last",
        license_number = "AAA12345"
        driver = get_user_model().objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            license_number=license_number
        )

        self.assertEqual(driver.username, username)
        self.assertEqual(driver.first_name, first_name)
        self.assertEqual(driver.last_name, last_name)
        self.assertEqual(driver.license_number, license_number)
