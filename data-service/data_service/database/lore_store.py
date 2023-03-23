from typing import Dict
from data_service.database.connection import get_db


def persist_lore(champ_id: str, lore: str):
    """
    Persist the lore for a given champion.
    :param champ_id: The champion ID to persist.
    :param lore: The lore to persist.
    """
    db = get_db()
    db["lore"].insert_one({"_id": champ_id, "lore": lore})


def persist_all_lore(champ_lore_by_id: Dict[str, str]):
    """
    Persist all lore for all champions.
    A destructive action! Will delete all lore and overwrite it.
    :param champ_lore_by_id: A dictionary of champion ID to lore.
    """
    db = get_db()
    db["lore"].drop()
    lore_docs = [
        {"_id": champ_id, "lore": lore} for champ_id, lore in champ_lore_by_id.items()
    ]
    db["lore"].insert_many(lore_docs)
