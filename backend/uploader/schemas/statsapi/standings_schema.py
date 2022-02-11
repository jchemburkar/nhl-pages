""" models player api reponse and player db rows """
from datetime import datetime
from marshmallow import Schema, fields, pre_load, pre_dump, post_dump
from uploader.schemas.shared import RawInfo

##############
# Raw Schema #
##############

class RawRecord(Schema):
    losses = fields.Integer()
    ot = fields.Integer()
    type = fields.Str()
    wins = fields.Integer()


class RawStreak(Schema):
    streakCode = fields.Str()
    streakNumber = fields.Integer()
    streakType = fields.Str()


class RawTeamStanding(Schema):
    conferenceRank = fields.Integer()
    conferenceL10Rank = fields.Integer()
    conferenceHomeRank = fields.Integer()
    conferenceRoadRank = fields.Integer()
    divisionHomeRank = fields.Integer()
    divisionL10Rank = fields.Integer()
    divisionRank = fields.Integer()
    divisionRoadRank = fields.Integer()
    goalsAgainst = fields.Integer()
    gamesPlayed = fields.Integer()
    goalsScored = fields.Integer()
    goalsFor = fields.Integer()
    lastUpdated = fields.DateTime()
    leagueRecord = fields.Nested(RawRecord)
    leagueRank = fields.Integer()
    leagueL10Rank = fields.Integer()
    leagueHomeRank = fields.Integer()
    leagueRoadRank = fields.Integer()
    points = fields.Integer()
    pointsPercentage = fields.Float()
    ppConferenceRank = fields.Integer()
    ppDivisionRank = fields.Integer()
    ppLeagueRank = fields.Integer()
    regulationWins = fields.Integer()
    row = fields.Integer()
    streak = fields.Nested(RawStreak)
    team = fields.Nested(RawInfo)
    wildCardRank = fields.Integer()

    @pre_load
    def preload(self, data, **kwargs):
        """ int cast 'ranks' """
        for k, v in data.items():
            if isinstance(v, str) and 'Rank' in k:
                data[k] = int(v)
        return data


class RawDivisonStanding(Schema):
    conference = fields.Nested(RawInfo)
    division = fields.Nested(RawInfo)
    league = fields.Nested(RawInfo)
    standingsType = fields.Str()
    teamRecords = fields.Nested(RawTeamStanding, many=True)


class RawStanding(Schema):
    copyright = fields.Str()
    records = fields.Nested(RawDivisonStanding, many=True)


#################
# Parsed Schema #
#################

class Standing(Schema):
    conference_rank = fields.Integer(attribute="conferenceRank")
    conference_l10_rank = fields.Integer(attribute="conferenceL10Rank")
    conference_home_rank = fields.Integer(attribute="conferenceHomeRank")
    conference_road_rank = fields.Integer(attribute="conferenceRoadRank")
    division_home_rank = fields.Integer(attribute="divisionHomeRank")
    division_l10_rank = fields.Integer(attribute="divisionL10Rank")
    division_rank = fields.Integer(attribute="divisionRank")
    division_road_rank = fields.Integer(attribute="divisionRoadRank")
    games_played = fields.Integer(attribute="gamesPlayed")
    goals_against = fields.Integer(attribute="goalsAgainst")
    goals_for = fields.Integer(attribute="goalsFor")
    last_updated = fields.DateTime(attribute="lastUpdated")
    league_id = fields.Integer(attribute="league.id")
    league_rank = fields.Integer(attribute="leagueRank")
    league_l10_rank = fields.Integer(attribute="leagueL10Rank")
    league_home_rank = fields.Integer(attribute="leagueHomeRank")
    league_road_rank = fields.Integer(attribute="leagueRoadRank")
    points = fields.Integer()
    points_percentage = fields.Float(attribute="pointsPercentage")
    pp_conference_rank = fields.Integer(attribute="ppConferenceRank")
    pp_division_rank = fields.Integer(attribute="ppDivisionRank")
    pp_league_rank = fields.Integer(attribute="ppLeagueRank")
    regulation_wins = fields.Integer(attribute="regualtionWins")
    row = fields.Integer()
    streak = fields.Str()
    team_id = fields.Integer(attribute="team.id")
    wild_card_rank = fields.Integer(attribute="wildCardRank")

    @pre_dump
    def predump(self, data, **kwargs):
        """ handle streak """
        data["streak"] = f"{data['streak']['streakCode']}{data['streak']['streakNumber']}"
        return data

    @post_dump
    def postdump(self, data, **kwargs):
        """ handle last updated """
        data["last_updated"] = data["last_updated"].split("+00:00")[0]
        return data
