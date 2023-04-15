import logging

log = logging.getLogger(__name__)

import os
from typing import Any, Dict, List, Text

import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.events import FollowupAction, SlotSet
from rasa_sdk.executor import CollectingDispatcher

DATA_SERVICE_URL = os.getenv("DATA_SERVICE_URL")


class ActionPopulateSummonerInfo(Action):
    def name(self) -> Text:
        return "action_populate_summoner_info"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        if (
            tracker.get_slot("summoner_name") is not None
            and tracker.get_slot("puuid") is not None
        ):
            return []

        # make call to data service using sender_id
        sender_id = tracker.sender_id
        res = requests.get(
            f"{DATA_SERVICE_URL}/summoner_info/by_discord_id?discord_id={sender_id}"
        )

        if res.status_code == 200:
            json = res.json()
            log.info(f"User with ID {sender_id} has a summoner name: {json['name']}")
            return [
                SlotSet("summoner_name", json["name"]),
                SlotSet("puuid", json["puuid"]),
            ]
        else:
            log.info(
                f"User with ID {sender_id} does not have a summoner name, asking for one"
            )
            dispatcher.utter_message(response="utter_dont_know_summoner_name")

        return [FollowupAction("summoner_name_form")]
