"""Additional functions for Viber bot."""
from functools import partial
from dotenv import load_dotenv
from geopy.geocoders import Nominatim
from viberbot.api.messages.data_types.location import Location


def dotenv_definer():
    load_dotenv('.env')


def get_address(location: Location) -> str:
    """Transcripting location coordinates to real address."""
    geolocator = Nominatim(user_agent="SushiPizzaBot")
    coordinates_transcriptor = partial(geolocator.reverse, language="ru")
    lat, lon = location.latitude, location.longitude
    return str(coordinates_transcriptor(f"{lat}, {lon}"))


def rich_message_consctructor(items: list) -> dict:
    """Pasting infromation from list of items to rich message template."""
    buttons = []
    for item in items:
        buttons.append(
            {
               "Columns": 5,
               "Rows": 3,
               "ActionType": "reply",
               "ActionBody": f"order-{item[0]}",
               "Image": item[1]
            }
        )
        buttons.append(
            {
               "Columns": 5,
               "Rows": 2,
               "Text": f"<font color=#323232><b>{item[0]}</b></font>"
                       f"<font color=#777777><br>{item[2]} </font><br>"
                       f"<font color=#6fc133><b>{item[3]}</b></font>",
               "ActionType": "reply",
               "ActionBody": f"order-{item[0]}",
               "TextSize": "medium",
               "TextVAlign": "middle",
               "TextHAlign": "left"
            }
        )
        buttons.append(
            {
               "Columns": 5,
               "Rows": 1,
               "ActionType": "reply",
               "ActionBody": f"order-{item[0]}",
               "Text": "<font color=#ffffff>Купить</font>",
               "TextSize": "large",
               "TextVAlign": "middle",
               "TextHAlign": "middle"
            }
        )
    template = {
          "Type": "rich_media",
          "ButtonsGroupColumns": 5,
          "ButtonsGroupRows": 6,
          "BgColor": "#FFFFFF",
          "Buttons": buttons
       }
    return template
