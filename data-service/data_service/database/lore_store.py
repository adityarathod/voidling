import logging

log = logging.getLogger(__name__)

from typing import List

from pydantic import BaseModel
from data_service.database.connection import get_db


class ChampLore(BaseModel):
    """
    A champion's lore.
    """

    id: str
    name: str
    lore: str


def get_lore_by_id(champ_id: str) -> ChampLore:
    """
    Get the lore for a given champion.
    :param champ_id: The champion ID to get the lore for.
    :return: The lore for the given champion.
    """
    db = get_db()
    doc = db["lore"].find_one({"id": champ_id})
    return ChampLore(**doc)


def persist_lore(lore: ChampLore):
    """
    Persist the lore for a given champion.
    :param champ_id: The champion ID to persist.
    :param lore: The lore to persist.
    """
    db = get_db()
    db["lore"].insert_one(lore.dict())


def persist_all_lore(lore: List[ChampLore]):
    """
    Persist all lore for all champions.
    A destructive action! Will delete all lore and overwrite it.
    :param champ_lore_by_id: A dictionary of champion ID to lore.
    """
    log.info("Persisting all lore")
    log.debug(f"{len(lore)} lore documents to persist")
    db = get_db()
    log.info("Dropping existing lore collection")
    db["lore"].drop()
    lore_docs = [l.dict() for l in lore]
    db["lore"].insert_many(lore_docs)
