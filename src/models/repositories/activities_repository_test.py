import pytest
import uuid
from .activities_repository import ActivitiesRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())
activity_id = str(uuid.uuid4())

#@pytest.mark.skip(reason="Interaction with database")
def test_registry_activity():
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)

    activity_infos = {
        "id":  activity_id,
        "trip_id": trip_id,
        "title": "conhecer tabacaria",
        "occurs_at": ""
    }

    activities_repository.registry_activity(activity_infos)

#@pytest.mark.skip(reason="Interaction with database")
def test_find_activities_from_trip():
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)
    activities = activities_repository.find_activities_from_trip(trip_id)
    print()
    print(activities)


