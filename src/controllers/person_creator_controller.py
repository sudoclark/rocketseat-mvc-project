from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface
from src.errors.http_types.http_bad_request import HttpBadRequestError
from .interfaces.person_creator_controller import PeopleCreatorControllerInterface

class PeopleCreatorController(PeopleCreatorControllerInterface):
    def __init__(self, people_repository: PeopleRepositoryInterface):
        self.__people_repository = people_repository

    def create_person(self, person_info: dict) -> dict:
        first_name = person_info["first_name"]
        last_name = person_info["last_name"]
        age = person_info["age"]
        pet_id = person_info["pet_id"]

        self.__validate_names(first_name, last_name)
        self.__insert_person_into_db(first_name, last_name, age, pet_id)
        response = self.__format_response(person_info)

        return response

    def __validate_names(self, first_name: str, last_name: str) -> None:
        if not first_name.isalpha() or not last_name.isalpha():
            raise HttpBadRequestError("Os nomes precisam ser caracteres de A-Z")

    def __insert_person_into_db(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
        self.__people_repository.insert_person(first_name, last_name, age, pet_id)

    def __format_response(self, person_info: dict) -> dict:
        return {
            "data": {
                "type": "Person",
                "count": 1,
                "attributes": person_info
            }
        }
