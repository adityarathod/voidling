import os
from typing import Optional

import requests
from pydantic import BaseModel

from data_service.riot_api.constants import RIOT_SUMMONER_API_ROOT

RIOT_API_KEY = os.getenv("RIOT_API_KEY")
SUMMONER_API_BY_NAME_ROOT = "/lol/summoner/v4/summoners/by-name/"


class RiotAPISummonerInfo(BaseModel):
    id: str
    accountId: str
    puuid: str
    name: str
    profileIconId: int
    revisionDate: int
    summonerLevel: int


def get_summoner_by_name(summoner_name: str) -> Optional[RiotAPISummonerInfo]:
    """
    Get the summoner info for a given summoner name.
    :param summoner_name: The summoner name to get the info for.
    :return: The summoner info for the given summoner name.
    """
    url = f"{RIOT_SUMMONER_API_ROOT}{SUMMONER_API_BY_NAME_ROOT}{summoner_name}"
    res = requests.get(url, headers={"X-Riot-Token": RIOT_API_KEY})
    if res.status_code != 200:
        return None
    return RiotAPISummonerInfo(**res.json())
