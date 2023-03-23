from bs4 import BeautifulSoup
import requests


LORE_BASE_URL = "https://universe-meeps.leagueoflegends.com/v1/en_us/champions/$champ_slug/index.json"


def scrape_single_champ_lore(champ_slug: str) -> str:
    """
    Scrape the lore for a single champion.
    :param champ_slug: The champion name slugified as it is in the universe lore API.
    :return: The lore for the champion.
    """
    lore_url = LORE_BASE_URL.replace("$champ_slug", champ_slug.lower())
    response = requests.get(lore_url)
    response.raise_for_status()
    response_json = response.json()
    lore_html = response_json["champion"]["biography"]["full"]
    soup = BeautifulSoup(lore_html, "html.parser")
    formatted_text = "\n\n".join(
        [paragraph.get_text() for paragraph in soup.find_all("p")]
    )
    return formatted_text
