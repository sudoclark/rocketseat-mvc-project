from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface
from .interfaces.pets_deleter_controller import PetDeleterControllerInterface

class PetDeleterController(PetDeleterControllerInterface):
    def __init__(self, pets_repository: PetsRepositoryInterface):
        self.__pets_repository = pets_repository

    def delete(self, name: str) -> None:
        self.__pets_repository.delete_pet_by_name(name)
