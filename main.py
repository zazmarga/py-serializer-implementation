import initial

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from car.models import Car
from car.serializers import CarSerializer
import io


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return JSONRenderer().render(serializer.data)


def deserialize_car_object(json: bytes) -> Car:
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    car = serializer.save()
    return car
