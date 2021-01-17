"""Additional functions for Viber bot."""
from functools import partial
from geopy.geocoders import Nominatim
from viberbot.api.messages.data_types.location import Location


def get_address(location: Location) -> str:
    """Transcripting location coordinates to real address."""
    geolocator = Nominatim(user_agent="SushiPizzaBot")
    coordinates_transcriptor = partial(geolocator.reverse, language="ru")
    lat, lon = location.latitude, location.longitude
    return str(coordinates_transcriptor(f"{lat}, {lon}"))
