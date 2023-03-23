import requests
import os

DDRAGON_ROOT = os.getenv("DDRAGON_ROOT_URL")


def make_request(url: str):
    """
    Makes a request to the given Riot Data Dragon URL and returns the response.
    """
    joined_url = DDRAGON_ROOT + url
    response = requests.get(joined_url)
    response.raise_for_status()
    return response
