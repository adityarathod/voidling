from sanic import Blueprint, Request, json

from data_service.database.summoner_store import (
    SummonerInfo,
    get_summoner_by_discord_id,
    persist_summoner,
)
from data_service.riot_api.summoner import get_summoner_by_name

bp = Blueprint("summoner_info", url_prefix="/summoner_info")


@bp.route("/by_discord_id", methods=["GET"])
async def get_summoner_info_by_id(request: Request):
    discord_id = request.get_args().get("discord_id")

    if not discord_id:
        return json({"error": "No discord id provided"}, status=400)

    # get summoner info from db
    summoner = get_summoner_by_discord_id(discord_id)

    if not summoner:
        return json({"error": "No summoner found for discord id"}, status=404)

    return json(summoner.dict())


@bp.route("/by_summoner_name", methods=["GET"])
async def get_summoner_info_by_name(request: Request):
    summoner_name = request.get_args().get("summoner_name")
    discord_id = request.get_args().get("discord_id")

    if not summoner_name:
        return json({"error": "No summoner name provided"}, status=400)
    if not discord_id:
        return json({"error": "No discord id provided"}, status=400)

    # get summoner info from Riot API
    raw_summoner = get_summoner_by_name(summoner_name)

    if not raw_summoner:
        return json({"error": "No summoner found for name"}, status=404)

    summoner = SummonerInfo(
        discord_id=discord_id,
        name=raw_summoner.name,
        puuid=raw_summoner.puuid,
    )

    # persist summoner info
    persist_summoner(summoner)

    return json(summoner.dict())
