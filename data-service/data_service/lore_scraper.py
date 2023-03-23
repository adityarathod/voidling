from data_service.data_dragon.champions import get_all_champs
from data_service.database.lore_store import persist_all_lore
from data_service.universe_lore.champ_slugs import get_champ_slugs
from data_service.universe_lore import scrape_single_champ_lore

LORE_BASE_URL = "https://universe.leagueoflegends.com/en_US/story/champion"
LORE_BASE_URL = (
    "https://universe-meeps.leagueoflegends.com/v1/en_us/champions/$champid/index.json"
)


def main():
    champ_slugs = get_champ_slugs()
    get_all_champs()
    all_lore = {cid: scrape_single_champ_lore(cid) for cid in champ_slugs}
    persist_all_lore(all_lore)


if __name__ == "__main__":
    main()
