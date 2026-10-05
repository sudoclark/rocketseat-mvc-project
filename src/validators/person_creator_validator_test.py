import pytest

from src.errors.http_types.http_unprocessable_entity import HttpUnprocessableEntityError
from .person_creator_validator import person_creator_validator

class MockRequest:
    def __init__(self, body):
        self.body = body

def test_person_creator_validator():
    request = MockRequest({
        "first_name": "John",
        "last_name": "Doe",
        "age": 27,
        "pet_id": 13
    })

    person_creator_validator(request)

def test_person_creator_validator_error_wrong_data_type():
    request = MockRequest({
        "first_name": "John",
        "last_name": "Doe",
        "age": "abc",
        "pet_id": 13
    })

    with pytest.raises(HttpUnprocessableEntityError):
        person_creator_validator(request)
