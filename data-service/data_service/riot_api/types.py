from typing import List

from pydantic import BaseModel


class MatchMetadata(BaseModel):
    dataVersion: str
    matchId: str
    participants: List[str]


class ParticipantInfo(BaseModel):
    assists: int
    baronKills: int
    bountyLevel: int
    champExperience: int
    champLevel: int
    championId: int
    championName: str
    championTransform: int
    consumablesPurchased: int
    damageDealtToBuildings: int
    damageDealtToObjectives: int
    damageDealtToTurrets: int
    damageSelfMitigated: int
    deaths: int
    detectorWardsPlaced: int
    doubleKills: int
    dragonKills: int
    firstBloodAssist: bool
    firstBloodKill: bool
    firstTowerAssist: bool
    firstTowerKill: bool
    gameEndedInEarlySurrender: bool
    gameEndedInSurrender: bool
    goldEarned: int
    goldSpent: int
    individualPosition: str
    inhibitorKills: int
    inhibitorTakedowns: int
    item0: int
    item1: int
    item2: int
    item3: int
    item4: int
    item5: int
    item6: int
    itemsPurchased: int
    killingSprees: int
    kills: int
    lane: str
    largestCriticalStrike: int
    largestKillingSpree: int
    largestMultiKill: int
    longestTimeSpentLiving: int
    magicDamageDealt: int
    magicDamageDealtToChampions: int
    magicDamageTaken: int
    neutralMinionsKilled: int
    nexusKills: int
    nexusTakedowns: int
    objectivesStolen: int
    objectivesStolenAssists: int
    participantId: int
    pentaKills: int
    perks: dict
    physicalDamageDealt: int
    physicalDamageDealtToChampions: int
    physicalDamageTaken: int
    profileIcon: int
    puuid: str
    quadraKills: int
    riotIdName: str
    riotIdTagline: str
    role: str
    sightWardsBoughtInGame: int
    spell1Casts: int
    spell2Casts: int
    spell3Casts: int
    spell4Casts: int
    summoner1Casts: int
    summoner1Id: int
    summoner2Casts: int
    summoner2Id: int
    summonerId: str
    summonerLevel: int
    summonerName: str
    teamEarlySurrendered: bool
    teamId: int
    teamPosition: str
    timeCCingOthers: int
    timePlayed: int
    totalDamageDealt: int
    totalDamageDealtToChampions: int
    totalDamageShieldedOnTeammates: int
    totalDamageTaken: int
    totalHeal: int
    totalHealsOnTeammates: int
    totalMinionsKilled: int
    totalTimeCCDealt: int
    totalTimeSpentDead: int
    totalUnitsHealed: int
    tripleKills: int
    trueDamageDealt: int
    trueDamageDealtToChampions: int
    trueDamageTaken: int
    turretKills: int
    turretTakedowns: int
    turretsLost: int
    unrealKills: int
    visionScore: int
    visionWardsBoughtInGame: int
    wardsKilled: int
    wardsPlaced: int
    win: bool


class ObjectiveDetail(BaseModel):
    first: bool
    kills: int


class ObjectivesInfo(BaseModel):
    baron: ObjectiveDetail
    champion: ObjectiveDetail
    dragon: ObjectiveDetail
    inhibitor: ObjectiveDetail
    riftHerald: ObjectiveDetail
    tower: ObjectiveDetail


class TeamInfo(BaseModel):
    bans: List[dict]
    objectives: ObjectivesInfo
    teamId: int
    win: bool


class MatchData(BaseModel):
    # match dto from Riot API
    metadata: MatchMetadata
    info: dict


class MatchInfo(BaseModel):
    gameCreation: int
    gameDuration: int
    gameMode: str
    gameType: str
    gameVersion: str
    mapId: int
    participants: List[ParticipantInfo]
    platformId: str
    queueId: int
    teams: List[TeamInfo]


class AllMatchInfo(BaseModel):
    metadata: MatchMetadata
    info: MatchInfo
