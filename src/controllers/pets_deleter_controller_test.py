from .pets_deleter_controller import PetDeleterController

def test_delete_pet(mocker):
    mock_repository = mocker.Mock()
    controller = PetDeleterController(mock_repository)

    controller.delete("Rex")

    mock_repository.delete_pet_by_name.assert_called_once_with("Rex")
