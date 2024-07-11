import uuid
import pytest
from src.models.settings.db_connection_handler import db_connection_handle
from .activities_repository import ActivitiesRepository

db_connection_handle.connect()
trip_id = str(uuid.uuid4())
link_id = str(uuid.uuid4())

def test_registry_activity():
    conn = db_connection_handle.get_connection()
    activities_to_repository = ActivitiesRepository(conn)
    
    activities_trips_infos = {
        "id" : link_id,
        "trip_id" : trip_id,
        "title" : "Natacao",
        "occurs_at" : "02-10-2023"
    }
    
    activities_to_repository.registry_activity(activities_trips_infos)


def test_find_activities_from_trip():
    conn = db_connection_handle.get_connection()
    activities_to_repository = ActivitiesRepository(conn)
    
    activities = activities_to_repository.find_activities_from_trip(trip_id)
    
    assert isinstance(activities, list)
    assert isinstance(activities[0], tuple)
