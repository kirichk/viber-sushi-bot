"""Additional functions for Viber bot."""
import os
from functools import partial
from dotenv import load_dotenv
from geopy.geocoders import Nominatim
from viberbot.api.messages.data_types.location import Location
from resources.media_map import MEDIA_MAP as MM


def dotenv_definer():
    load_dotenv('.env')


def get_address(location: Location) -> str:
    """Transcripting location coordinates to real address."""
    geolocator = Nominatim(user_agent="SushiPizzaBot")
    coordinates_transcriptor = partial(geolocator.reverse, language="ru")
    lat, lon = location.latitude, location.longitude
    return str(coordinates_transcriptor(f"{lat}, {lon}"))


def load_images_from_folder(folder: str) -> list:
    images = []
    for filename in os.listdir(folder):
        path = 'file:///' + os.path.abspath(os.path.join(folder, filename))
        formatted_filename = folder.split('/')[2] + filename
        images.append([path, MM[formatted_filename]])
    return images


def rich_message_consctructor(folder: str) -> dict:
    """Pasting infromation from list of items to rich message template."""
    items = load_images_from_folder(folder)
    buttons = []
    for item in items:
        buttons.append(
            {
                "Columns": 5,
                "Rows": 5,
                "ActionType": "reply",
                "ActionBody": f"order-{item[0]}",
                "Image": item[0],
                "Text": item[1],
                "TextOpacity": 0,
            }
        )
    template = {
        "Type": "rich_media",
        "ButtonsGroupColumns": 5,
        "ButtonsGroupRows": 5,
        "BgColor": "#FFFFFF",
        "Buttons": buttons
    }
    return template


def keyboard_consctructor(items: list) -> dict:
    """Pasting infromation from list of items to keyboard menu template."""
    keyboard = {
        "DefaultHeight": False,
        "BgColor": "#FFFFFF",
        "Type": "keyboard",
        "Buttons": [{
                "Columns": 3,
                "Rows": 1,
                "BgColor": "#e6f5ff",
                "BgLoop": True,
                "ActionType": "reply",
                "ActionBody": item[0],
                "ReplyType": "message",
                "Text": item[1]
        } for item in items]
    }
    return keyboard


if __name__ == '__main__':
    print(load_images_from_folder('resources/images/combo'))
