import logging

log = logging.getLogger(__name__)

from typing import Optional

from pydantic import BaseModel

from data_service.database.connection import get_db


class SummonerInfo(BaseModel):
    """
    Champion info, from the Riot API.
    """

    discord_id: str
    name: str
    puuid: str


def get_summoner_by_discord_id(discord_id: str) -> Optional[SummonerInfo]:
    """
    Get the summoner info for a given summoner name.
    :param summoner_name: The summoner name to get the info for.
    :return: The summoner info for the given summoner name.
    """
    db = get_db()
    doc = db["summoners"].find_one({"discord_id": discord_id})
    if doc is None:
        return None
    lore = SummonerInfo(**doc)
    return lore


def persist_summoner(summoner: SummonerInfo):
    """
    Persist the summoner info for a given summoner.
    :param summoner: The summoner info to persist.
    """
    db = get_db()
    db["summoners"].find_one_and_replace(
        {"discord_id": summoner.discord_id}, summoner.dict(), upsert=True
    )
