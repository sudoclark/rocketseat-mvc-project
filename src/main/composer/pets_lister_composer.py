from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pets_repository import PetsRepository
from src.controllers.pets_lister_controller import PetsListerController
from src.views.pets_lister_view import PetsListerView

def pets_lister_composer():
    model = PetsRepository(db_connection_handler)
    controller = PetsListerController(model)
    view = PetsListerView(controller)

    return view
