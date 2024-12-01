import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "car_service.settings")

django.setup()


from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from car.models import Car
from car.serializers import CarSerializer
import io


def serialize_car_object(car):
    serializer = CarSerializer(car)
    return JSONRenderer().render(serializer.data)


def deserialize_car_object(json_data):
    stream = io.BytesIO(json_data)
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    car = serializer.save()
    return car
