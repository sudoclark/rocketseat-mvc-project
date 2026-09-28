from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface
from src.models.sqlite.entities.pets import PetsTable

class PetsListerController:
    def __init__(self, pets_repository: PetsRepositoryInterface):
        self.__pets_repository = pets_repository

    def list(self) -> dict:
        pets = self.__get_pets_from_db()
        response = self.__format_response(pets)

        return response

    def __get_pets_from_db(self) -> list[PetsTable]:
        pets = self.__pets_repository.list_pets()

        return pets

    def __format_response(self, pets: list[PetsTable]) -> dict:
        formatted_response = [{"pet_name": pet.name, "pet_type": pet.type, "pet_id": pet.id} for pet in pets]

        return {
            "data": {
                "type": "Pets",
                "count": len(formatted_response),
                "attributes": formatted_response
            }
        }
