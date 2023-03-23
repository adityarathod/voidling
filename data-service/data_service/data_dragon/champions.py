from typing import List
from pydantic import BaseModel
from data_service.data_dragon.util import make_request


class Champion(BaseModel):
    version: str
    id: str
    key: str
    title: str
    blurb: str


def get_all_champs() -> List[Champion]:
    champs_response = make_request("/champion.json")
    champs_json = champs_response.json()
    champs_data_raw = champs_json["data"]
    all_champs = [Champion(**champ) for champ in champs_data_raw.values()]
    return all_champs
