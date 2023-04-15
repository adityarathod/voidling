import logging

log = logging.getLogger(__name__)

import os
from typing import Any, Dict, Text

import requests
from rasa_sdk import FormValidationAction, Tracker
from rasa_sdk.executor import CollectingDispatcher

DATA_SERVICE_URL = os.getenv("DATA_SERVICE_URL")


class ValidateSummonerNameForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_summoner_name_form"

    def validate_summoner_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate summoner name value."""
        log.info(f"Validating summoner name: {slot_value}")
        sender_id = tracker.sender_id
        summoner_name = slot_value
        res = requests.get(
            f"{DATA_SERVICE_URL}/summoner_info/by_summoner_name?discord_id={sender_id}&summoner_name={summoner_name}"
        )

        if res.status_code == 200:
            json = res.json()
            log.info(f"Summoner name {summoner_name} is valid")
            return {"summoner_name": summoner_name, "puuid": json["puuid"]}

        log.info(f"Summoner name {summoner_name} is not valid")
        return {"summoner_name": None}
