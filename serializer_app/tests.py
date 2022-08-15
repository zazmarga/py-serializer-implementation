from django.test import TestCase

from serializer_app.models import Car
from main import serialize_car_object, deserialize_car_object
from serializer_app.serializers import CarSerializer


class TestSerializer(TestCase):
    def setUp(self):
        self.payload = {
            "manufacturer": "Audi",
            "model": "A4",
            "horse_powers": 200,
            "needs_to_be_fixed": True,
            "problem_description": "test description",
        }

        self.serializer_data = {
            "manufacturer": "Mercedes",
            "model": "CLS",
            "horse_powers": 300,
            "needs_to_be_fixed": False,
            "problem_description": "test description",
        }

        self.car = Car.objects.create(**self.payload)
        self.serializer = CarSerializer(instance=self.car)

        self.data = self.serializer.data

    def test_contains_expected_fields(self):
        self.assertEqual(
            set(self.data.keys()),
            {
                "id",
                "manufacturer",
                "model",
                "horse_powers",
                "needs_to_be_fixed",
                "problem_description",
            },
        )

    def test_serializer_fields(self):
        self.assertEqual(self.data["manufacturer"], self.payload["manufacturer"])
        self.assertEqual(self.data["model"], self.payload["model"])
        self.assertEqual(self.data["horse_powers"], self.payload["horse_powers"])
        self.assertEqual(
            self.data["needs_to_be_fixed"], self.payload["needs_to_be_fixed"]
        )
        self.assertEqual(
            self.data["problem_description"], self.payload["problem_description"]
        )

    def test_if_serializer_has_min_value(self):
        self.serializer_data["horse_powers"] = 0

        serializer = CarSerializer(data=self.serializer_data)

        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors), {"horse_powers"})

    def test_if_serializer_has_max_value(self):
        self.serializer_data["horse_powers"] = 2000

        serializer = CarSerializer(data=self.serializer_data)

        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors), {"horse_powers"})

    def test_manufacturer_max_length(self):
        self.serializer_data["manufacturer"] = (
            "Extremely long test manufacturer Extremely long test manufacturer "
        )

        serializer = CarSerializer(data=self.serializer_data)

        self.assertFalse(
            serializer.is_valid(), "Max length of manufacturer field should be 55"
        )
        self.assertEqual(set(serializer.errors), {"manufacturer"})

    def test_model_max_length(self):
        self.serializer_data["manufacturer"] = (
            "Extremely long test model "
            "Extremely long test model "
            "Extremely long test model "
        )

        serializer = CarSerializer(data=self.serializer_data)

        self.assertFalse(
            serializer.is_valid(), "Max length of model field should be 55"
        )
        self.assertEqual(set(serializer.errors), {"manufacturer"})

    def test_if_problem_description_is_not_required(self):
        self.serializer_data.pop("problem_description")

        serializer = CarSerializer(data=self.serializer_data)

        self.assertTrue(
            serializer.is_valid(), "problem_description field should not be required"
        )


class TestSerializerFunctions(TestCase):
    def setUp(self) -> None:
        self.payload = {
            "manufacturer": "Audi",
            "model": "A4",
            "horse_powers": 200,
            "needs_to_be_fixed": True,
            "problem_description": "test description",
        }

        self.car = Car.objects.create(**self.payload)
        self.json = b'{"id":9,"manufacturer":"Audi","model":"A4",' \
                    b'"horse_powers":200,"needs_to_be_fixed":true,"problem_description":"test description"}'

    def test_serialize_car(self):
        result = '{"id":1,"manufacturer":"Audi","model":"A4","horse_powers":200,' \
                 '"needs_to_be_fixed":true,"problem_description":"test description"}'

        self.assertEqual(serialize_car_object(car=self.car), bytes(result, "utf-8"))

    def test_deserialize_car(self):
        serializer = deserialize_car_object(self.json)

        self.assertTrue(serializer.is_valid())
        self.assertEqual(
            serializer.data,
            {
                "manufacturer": "Audi",
                "model": "A4",
                "horse_powers": 200,
                "needs_to_be_fixed": True,
                "problem_description": "test description",
            },
        )
