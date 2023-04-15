import logging

log = logging.getLogger(__name__)

import os
from typing import List, Optional

import requests

from data_service.riot_api.constants import RIOT_MATCH_API_ROOT
from data_service.riot_api.types import AllMatchInfo

RIOT_API_KEY = os.getenv("RIOT_API_KEY")

MATCH_API_GET_IDS_ROOT = "/lol/match/v5/matches/by-puuid/$puuid/ids"
MATCH_API_GET_MATCH_ROOT = "/lol/match/v5/matches/$match_id"

MatchIDs = List[str]


def get_match_ids(puuid: str, num_matches: int = 10) -> Optional[MatchIDs]:
    """
    Get the summoner info for a given summoner name.
    :param summoner_name: The summoner name to get the info for.
    :return: The summoner info for the given summoner name.
    """
    url = f"{RIOT_MATCH_API_ROOT}{MATCH_API_GET_IDS_ROOT}".replace("$puuid", puuid)
    url += f"?start=0&count={num_matches}"
    res = requests.get(url, headers={"X-Riot-Token": RIOT_API_KEY})
    if res.status_code != 200:
        log.error(f"[{res.status_code}] Error retrieving match ids: {res.text}")
        return None
    json = res.json()
    # check if the response is a list of strings
    if not isinstance(json, list) or not all(isinstance(x, str) for x in json):
        return None
    return json


def get_match(match_id: str) -> Optional[AllMatchInfo]:
    """
    Get the summoner info for a given summoner name.
    :param summoner_name: The summoner name to get the info for.
    :return: The summoner info for the given summoner name.
    """
    url = f"{RIOT_MATCH_API_ROOT}{MATCH_API_GET_MATCH_ROOT}".replace(
        "$match_id", match_id
    )
    res = requests.get(url, headers={"X-Riot-Token": RIOT_API_KEY})
    if res.status_code != 200:
        log.error(f"[{res.status_code}] Error retrieving match: {res.text}")
        return None
    return AllMatchInfo(**res.json())
