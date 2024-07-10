import pytest
import uuid
from .links_repository import LinksRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())
id = str(uuid.uuid4())

#@pytest.mark.skip(reason="Interaction with database")
def test_registry_link():
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)

    links_infos = {
        "id":  id,
        "trip_id": trip_id,
        "link": "www.google.com.br",
        "title": "Meu titulo"
    }

    links_repository.registry_link(links_infos)

#@pytest.mark.skip(reason="Interaction with database")
def test_find_links_by_trip():
    conn = db_connection_handler.get_connection()
    link_repository = LinksRepository(conn)
    links = link_repository.find_links_from_trip("c3af3fe0-ddba-4869-afed-e398b8f6f3bd")
    print()
    print(links)


