import os
from typing import Any, Dict, List, Text

import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

DATA_SERVICE_URL = os.getenv("DATA_SERVICE_URL")


class ActionLoreQuery(Action):
    def name(self) -> Text:
        return "action_lore_query"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        # make call to data service using text
        msg = tracker.latest_message["text"]
        # get response from data service
        res = requests.post(f"{DATA_SERVICE_URL}/lore_question", json={"question": msg})
        json = res.json()
        dispatcher.utter_message(
            text=json["answer"], json_message={"confidence": json["confidence"]}
        )
        return []
