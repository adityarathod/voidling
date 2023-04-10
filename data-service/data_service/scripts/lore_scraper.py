import logging

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

from typing import List, Tuple

from data_service.data_dragon.champions import Champion, get_all_champs
from data_service.database import ChampLore, persist_all_lore
from data_service.universe_lore import ChampSlug, get_champ_slugs, get_single_champ_lore


def add_ids_to_champ_lore(
    champ_lore: List[Tuple[ChampSlug, str]], champs: List[Champion]
) -> List[ChampLore]:
    """
    Add champion IDs to lore entries.
    :param champ_lore: A list of tuples of champion slugs and associated lore.
    :param champs: A list of all champions.
    :return: A list of all champion lore with IDs.
    """
    log.info("Adding champion IDs to lore entries")
    champs_by_name = {champ.name: champ for champ in champs}

    all_lore: List[ChampLore] = []
    for champ_slug, lore in champ_lore:
        # fix apostrophe error with K'Sante and Bel'Veth
        clean_name = champ_slug.name.replace("’", "'")
        champ_id = champs_by_name[clean_name].id
        lore_obj = ChampLore(id=champ_id, name=champ_slug.name, lore=lore)
        all_lore.append(lore_obj)

    return all_lore


def main():
    champ_slugs = get_champ_slugs()
    all_champs = get_all_champs()
    raw_lore = [(slug, get_single_champ_lore(slug)) for slug in champ_slugs]
    persist_all_lore(add_ids_to_champ_lore(raw_lore, all_champs))


if __name__ == "__main__":
    main()
