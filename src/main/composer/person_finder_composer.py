from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.people_repository import PeopleRepository
from src.controllers.people_finder_controller import PeopleFinderController
from src.views.people_finder_view import PeopleFinderView

def person_finder_composer():
    model = PeopleRepository(db_connection_handler)
    controller = PeopleFinderController(model)
    view = PeopleFinderView(controller)

    return view
