import pytest

from .person_creator_controller import PeopleCreatorController

class MockRepository:
    def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int): pass

def test_create_person():
    person_info = {
        "first_name": "Maria",
        "last_name": "Silva",
        "age": 38,
        "pet_id": 123
    }

    mock_repository = MockRepository()
    controller = PeopleCreatorController(mock_repository)
    response = controller.create_person(person_info)

    assert response["data"]["type"] == "Person"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == person_info

def test_create_person_error():
    person_info = {
        "first_name": "Maria123",
        "last_name": "Silva",
        "age": 38,
        "pet_id": 123
    }

    mock_repository = MockRepository()
    controller = PeopleCreatorController(mock_repository)

    with pytest.raises(Exception):
        controller.create_person(person_info)
