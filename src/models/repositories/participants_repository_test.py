import pytest
import uuid
from .participants_repository import ParticipantsRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())
participant_id = str(uuid.uuid4())
@pytest.mark.skip(reason="Interaction with database")
def test_registry_participant():
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)

    participants_infos = {
        "id": participant_id,
        "trip_id": trip_id,
        "emails_to_invite_id": participant_id,
        "name": "PEDRO"
    }
    participants_repository.registry_participant(participants_infos)


@pytest.mark.skip(reason="Interaction with database")
def test_find_trip_by_id():
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    print()
    print(participants_repository.find_participants_from_trip(trip_id))


@pytest.mark.skip(reason="Interaction with database")
def test_update_trip_status():
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)

    participants_repository.update_participant_status(trip_id)
