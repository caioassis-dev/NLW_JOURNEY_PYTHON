import uuid
import pytest
from src.models.settings.db_connection_handler import db_connection_handle
from .links_repository import LinksToRepository

db_connection_handle.connect()
trip_id = str(uuid.uuid4())
link_id = str(uuid.uuid4())

@pytest.mark.skip(reason="interacao com o banco")
def test_registry_links():
    conn = db_connection_handle.get_connection()
    links_to_repository = LinksToRepository(conn)

    link_trips_infos = {
        "id" : link_id,
        "trip_id": trip_id, 
        "link": "www.museuarte.com",
        "title": "Museu Arte",
    }
    
    links_to_repository.registry_links(link_trips_infos)

@pytest.mark.skip(reason="interacao com o banco")
def test_find_link_from_trip():
    conn = db_connection_handle.get_connection()
    links_to_repository = LinksToRepository(conn)
    
    links = links_to_repository.find_link_from_trip(trip_id)

    assert isinstance(links, list)
    assert isinstance(links[0], tuple)