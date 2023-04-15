from pydantic import BaseModel
from sanic import Blueprint, Request, json
from sanic.log import logger

from data_service.riot_api.match import get_match, get_match_ids
from data_service.riot_api.types import AllMatchInfo

bp = Blueprint("match_history", url_prefix="/match_history")


class MatchSummary(BaseModel):
    match_id: str
    game_duration: int
    champion: str
    kills: int
    deaths: int
    assists: int
    win: bool
    damage_dealt: int
    team_damage: int
    team_damage_percent: float


def summarize_match(match: AllMatchInfo, puuid: str) -> MatchSummary:
    participant = next(p for p in match.info.participants if p.puuid == puuid)
    total_team_damage = sum(
        [
            p.totalDamageDealtToChampions
            for p in match.info.participants
            if p.teamId == participant.teamId
        ]
    )
    return MatchSummary(
        **{
            "match_id": match.metadata.matchId,
            "game_duration": match.info.gameDuration,
            "champion": participant.championName,
            "kills": participant.kills,
            "deaths": participant.deaths,
            "assists": participant.assists,
            "win": participant.win,
            "damage_dealt": participant.totalDamageDealtToChampions,
            "team_damage": total_team_damage,
            "team_damage_percent": (
                0
                if total_team_damage is 0
                else participant.totalDamageDealtToChampions / total_team_damage
            ),
        }
    )


@bp.route("/", methods=["GET"])
async def get_match_history(request: Request):
    puuid = request.get_args().get("puuid")
    num_matches = int(request.get_args().get("num_matches"))

    if not puuid:
        return json({"error": "No puuid provided"}, status=400)

    match_ids = get_match_ids(puuid, num_matches if num_matches else 5)

    if match_ids is None:
        return json({"error": "No matches found for puuid"}, status=404)

    matches = [get_match(m) for m in match_ids]
    match_summaries = [summarize_match(m, puuid).dict() for m in matches]

    return json(match_summaries)
