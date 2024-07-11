import uuid
import pytest
from src.models.settings.db_connection_handler import db_connection_handle
from .participants_repository import ParticipantsRepository

db_connection_handle.connect()
trip_id = str(uuid.uuid4())
link_id = str(uuid.uuid4())
participant_id = str(uuid.uuid4())

def test_registry_participant():
    conn = db_connection_handle.get_connection()
    participants_to_repository = ParticipantsRepository(conn)
    
    participants_infos = {
        "id" : link_id,
        "trip_id" : trip_id,
        "emails_to_invite_id"  : "paula@teste.com",
        "name" : "Paula"
    }
    
    participants_to_repository.registry_participant(participants_infos)
    
def test_find_participants_from_trip():
    conn = db_connection_handle.get_connection()
    participants_to_repository = ParticipantsRepository(conn)
    
    participants = participants_to_repository.find_participants_from_trip(trip_id)
    print()
    print(participants)
    

def test_update_participant_status():
    conn = db_connection_handle.get_connection()
    participants_repository = ParticipantsRepository(conn)
    
    participants_repository.update_participant_status(link_id)  
