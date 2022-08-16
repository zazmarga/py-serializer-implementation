from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    pass


def deserialize_car_object(json: bytes) -> CarSerializer:
    pass
