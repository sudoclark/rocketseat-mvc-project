from abc import ABC, abstractmethod

class PeopleCreatorControllerInterface(ABC):

    @abstractmethod
    def create_person(self, person_info: dict) -> dict:
        pass
