import logging

log = logging.getLogger(__name__)

import requests
from bs4 import BeautifulSoup

from data_service.universe_lore.champ_slugs import ChampSlug

LORE_BASE_URL = "https://universe-meeps.leagueoflegends.com/v1/en_us/champions/$champ_slug/index.json"


def get_single_champ_lore(champ_slug: ChampSlug) -> str:
    """
    Obtain and parse the lore for a single champion.
    :param champ_slug: The champion name slug object.
    :return: The lore for the champion.
    """
    log.info(f"Getting lore for {champ_slug.name}")
    lore_url = LORE_BASE_URL.replace("$champ_slug", champ_slug.slug.lower())
    response = requests.get(lore_url)
    response.raise_for_status()
    response_json = response.json()
    log.info("Extracting lore HTML from response")
    lore_html = response_json["champion"]["biography"]["full"]
    soup = BeautifulSoup(lore_html, "html.parser")
    log.info("Outputting cleaner lore text")
    formatted_text = "\n\n".join(
        [paragraph.get_text() for paragraph in soup.find_all("p")]
    )
    return formatted_text
