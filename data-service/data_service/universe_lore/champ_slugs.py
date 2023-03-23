import logging

log = logging.getLogger(__name__)

import requests
from typing import List
from pydantic import BaseModel


CHAMP_SLUGS_URL = (
    "https://universe-meeps.leagueoflegends.com/v1/en_us/search/index.json"
)


class ChampSlug(BaseModel):
    name: str
    slug: str


def get_champ_slugs() -> List[ChampSlug]:
    """
    Get all champion slugs.
    :return: A list of all champion slugs.
    """
    log.info("Getting all champion slugs from Universe Lore API")
    response = requests.get(CHAMP_SLUGS_URL)
    response.raise_for_status()
    response_json = response.json()
    champ_descriptions = response_json["champions"]
    log.debug("Validating all champ slug data against model")
    champ_slugs = [ChampSlug(**entry) for entry in champ_descriptions]
    return champ_slugs
