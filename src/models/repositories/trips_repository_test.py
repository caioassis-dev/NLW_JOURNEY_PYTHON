import pytest
import uuid
from datetime import datetime, timedelta
from .trips_repository import TripsRepository
from src.models.settings.db_connection_handler import db_connection_handle

db_connection_handle.connect()
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="interacao com o banco")
def test_create_trip():
    conn = db_connection_handle.get_connection()
    trips_repository = TripsRepository(conn)
    
    trips_infos = {
        "id" : trip_id,
        "destination": "Disney", 
        "start_date": datetime.strptime("11-01-2024", "%d-%m-%Y"),
        "end_date": datetime.strptime("11-01-2024", "%d-%m-%Y") + timedelta(days=7),
        "owner_name": 'Pedro',
        "owner_email": "pedro@email.com"
    }
    
    trips_repository.create_trip(trips_infos)
    
@pytest.mark.skip(reason="interacao com o banco")  
def test_find_trip_by_id():
    conn = db_connection_handle.get_connection()
    trips_repository = TripsRepository(conn)
    
    trip = trips_repository.find_trip_by_id(trip_id)
    
    
@pytest.mark.skip(reason="interacao com o banco")
def test_update_trip_status():
    conn = db_connection_handle.get_connection()
    trips_repository = TripsRepository(conn)
    
    trips_repository.update_trip_status(trip_id)  
    

