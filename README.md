# Serializer Implementation

- **Please note:** read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md)
before start.

In this task, you should implement a serializer `CarSerializer` for the `Car` model in `serializers.py`.

The `Car` model has the following fields:
- manufacturer (with the max_length of 55);
- model (with the max_length of 55);
- horse_powers (with the min and max validators of 55);
- needs_to_be_fixed;
- problem_description (can be null).

Serializer should be created using **serializers.Serializer**.
**Please note:** `horse_powers` field should have min and max values, `manufacturer` and `model` should have max_lenght 55
and `problem_description` should not be required.

Also, you should implement 2 functions that use `CarSerializer` in `main.py`:
- the first one `serialize_car_object` accepts `Car` object and returns `json` with its data.
- the second one `deserialize_car_object` accepts `json` and returns serializer with data from `json`.
