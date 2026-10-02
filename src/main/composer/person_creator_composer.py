from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.people_repository import PeopleRepository
from src.controllers.person_creator_controller import PeopleCreatorController
from src.views.people_creator_view import PeopleCreatorView

def person_creator_composer():
    model = PeopleRepository(db_connection_handler)
    controller = PeopleCreatorController(model)
    view = PeopleCreatorView(controller)

    return view
