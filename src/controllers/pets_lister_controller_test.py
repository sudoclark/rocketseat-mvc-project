from src.models.sqlite.entities.pets import PetsTable
from .pets_lister_controller import PetsListerController

class MockRepository:
    def list_pets(self):
        return [
            PetsTable(name="Fluffy", type="Cat", id=2),
            PetsTable(name="Buddy", type="Dog", id=35)
        ]

def test_list_pets():
    controller = PetsListerController(MockRepository())
    pets = controller.list()

    expected_response = {
        "data": {
            "type": "Pets",
            "count": 2,
            "attributes": [
                {"pet_name": "Fluffy", "pet_type": "Cat", "pet_id": 2},
                {"pet_name": "Buddy", "pet_type": "Dog", "pet_id": 35},
            ]
        }
    }

    assert pets == expected_response
