import requests
from typing import List


CHAMP_SLUGS_URL = (
    "https://universe-meeps.leagueoflegends.com/v1/en_us/search/index.json"
)


def get_champ_slugs() -> List[str]:
    """
    Get all champion slugs.
    :return: A list of all champion slugs.
    """
    response = requests.get(CHAMP_SLUGS_URL)
    response.raise_for_status()
    response_json = response.json()
    champ_descriptions = response_json["champions"]
    champ_slugs = [champ["slug"] for champ in champ_descriptions]
    return champ_slugs
