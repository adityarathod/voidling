import os
from typing import List

import requests

from voidling_discord.message_processor import RasaMessage

RASA_SERVER_URL = os.getenv("RASA_SERVER_URL")
RASA_MESSAGE_URL = f"{RASA_SERVER_URL}/webhooks/rest/webhook"


def send_receive_messages(message_text: str, sender: str) -> List[RasaMessage]:
    global RASA_MESSAGE_URL
    result = requests.post(
        RASA_MESSAGE_URL,
        json={"message": message_text, "sender": sender},
        headers={"Content-Type": "application/json"},
    )
    result.raise_for_status()
    raw_json = result.json()
    if not isinstance(raw_json, list):
        raise ValueError("Expecting a list of responses from Rasa")
    return [RasaMessage(**message) for message in raw_json]
