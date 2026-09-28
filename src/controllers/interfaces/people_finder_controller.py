from abc import ABC, abstractmethod

class PeopleFinderControllerInterface(ABC):

    @abstractmethod
    def find(self, person_id: int) -> dict:
        pass
