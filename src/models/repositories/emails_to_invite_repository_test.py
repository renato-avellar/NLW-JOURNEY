import pytest
import uuid
from .emails_to_invite_repository import EmailsToInviteRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
email_id = str(uuid.uuid4())
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="Interaction with database")
def test_registry_email():
    conn = db_connection_handler.get_connection()
    email_repository = EmailsToInviteRepository(conn)

    emails_infos = {
        "id": email_id,
        "trip_id": trip_id,
        "email": "jaozin@email.com"
    }

    email_repository.registry_email(emails_infos)

@pytest.mark.skip(reason="Interaction with database")
def test_find_trip_by_id():
    conn = db_connection_handler.get_connection()
    email_repository = EmailsToInviteRepository(conn)
    emails = email_repository.find_emails_from_trip(trip_id)
    print()
    print(emails)


