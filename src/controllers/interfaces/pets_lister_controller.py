from abc import ABC, abstractmethod

class PetsListerControllerInterface(ABC):

    @abstractmethod
    def list(self) -> dict:
        pass
