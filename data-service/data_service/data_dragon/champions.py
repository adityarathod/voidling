import logging

log = logging.getLogger(__name__)

from typing import List

from pydantic import BaseModel

from data_service.data_dragon.util import make_request


class Champion(BaseModel):
    """
    A model for a champion. Exposes a subset of fields from Data Dragon.
    """

    version: str
    id: str
    name: str
    key: str
    title: str
    blurb: str


def get_all_champs() -> List[Champion]:
    """
    Get all champions from Data Dragon.
    :return: A list of all champions.
    """
    log.info("Getting all champions from Data Dragon")
    champs_response = make_request("/champion.json")
    champs_json = champs_response.json()
    champs_data_raw = champs_json["data"]
    log.debug("Validating all champ data against model")
    all_champs = [Champion(**champ) for champ in champs_data_raw.values()]
    log.info(f"Found {len(all_champs)} champions")
    return all_champs
