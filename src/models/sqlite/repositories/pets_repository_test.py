from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.sqlite.entities.pets import PetsTable
from .pets_repository import PetsRepository

class MockConnection:
    def __init__(self):
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(PetsTable)],
                    [PetsTable(name="dog", type="dog"), PetsTable(name="cat", type="cat")]
                )
            ]
        )

    def __enter__(self): return self
    def __exit__(self, exc_type, exc, tb): pass


def test_list_pets():
    mock_connection = MockConnection()
    repo = PetsRepository(mock_connection)

    response = repo.list_pets()

    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.all.assert_called_once()

    assert response[0].name == "dog"

def test_delete_pet():
    mock_connection = MockConnection()
    repo = PetsRepository(mock_connection)
    repo.delete_pet_by_name("pet_name")

    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.filter.assert_called_once_with(PetsTable.name == "pet_name")
    mock_connection.session.delete.assert_called_once()
