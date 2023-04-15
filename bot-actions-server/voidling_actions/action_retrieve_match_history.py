import logging

log = logging.getLogger(__name__)

import os
from typing import Any, Dict, List, Text

import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

DATA_SERVICE_URL = os.getenv("DATA_SERVICE_URL")


class ActionRetrieveMatchHistory(Action):
    def name(self) -> Text:
        return "action_retrieve_match_history"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        summoner_name = tracker.get_slot("summoner_name")
        puuid = tracker.get_slot("puuid")
        num_matches = tracker.get_slot("num_matches")

        # null check
        if summoner_name is None or puuid is None or num_matches is None:
            return []

        # make call to data service
        res = requests.get(
            f"{DATA_SERVICE_URL}/match_history?puuid={puuid}&num_matches={num_matches}"
        )

        dispatcher.utter_message(text=f"Here are your last {num_matches} matches:")
        for idx, match_summary in enumerate(res.json()):
            time_mins = match_summary["game_duration"] // 60
            time_secs = match_summary["game_duration"] % 60
            win_text = "🏆 **Won**" if match_summary["win"] else "❌ **Lost**"
            dmg_percent = match_summary["team_damage_percent"] * 100
            text_template = f"""[{win_text}] {idx+1}. Match ID **{match_summary['match_id']}** ({time_mins}:{time_secs:02})
            - K/D/A: {match_summary['kills']}/{match_summary['deaths']}/{match_summary['assists']}
            - Champion: {match_summary['champion']}
            - Damage: {match_summary['damage_dealt']} ({dmg_percent:.2f}% of team damage)
            """
            dispatcher.utter_message(text=text_template)
            # dispatcher.utter_message(json_message=match_summary)

        if res.status_code != 200:
            log.error(f"[{res.status_code}] Error retrieving match history: {res.text}")
            dispatcher.utter_message(response="utter_match_history_error")
            return []

        # reset slots
        return [
            SlotSet("num_matches", None),
        ]
