""" parses output of query into dict for FE """
from marshmallow import Schema, fields

class StandingSchema(Schema):
    conferenceId = fields.Integer(attribute="conference_id")
    conferenceName = fields.Str(attribute="conference_name")
    conferenceRank = fields.Integer(attribute="StatsapiStanding.conference_rank")
    conferenceL10Rank = fields.Integer(attribute="StatsapiStanding.conference_l10_rank")
    conferenceHomeRank = fields.Integer(attribute="StatsapiStanding.conference_home_rank")
    divisionId = fields.Integer(attribute="division_id")
    divisionName = fields.Str(attribute="division_name")
    conferenceRoadRank = fields.Integer(attribute="StatsapiStanding.conference_road_rank")
    divisionHomeRank = fields.Integer(attribute="StatsapiStanding.division_home_rank")
    divisionL10Rank = fields.Integer(attribute="StatsapiStanding.division_l_10_rank")
    divisionRank = fields.Integer(attribute="StatsapiStanding.division_rank")
    divisionRoadRank = fields.Integer(attribute="StatsapiStanding.division_road_rank")
    gamesPlayed = fields.Integer(attribute="StatsapiStanding.games_played")
    goalsAgainst = fields.Integer(attribute="StatsapiStanding.goals_against")
    goalsFor = fields.Integer(attribute="StatsapiStanding.goals_for")
    lastUpdated = fields.DateTime(attribute="StatsapiStanding.last_updated")
    leagueId = fields.Integer(attribute="StatsapiStanding.league_id")
    leagueRank = fields.Integer(attribute="StatsapiStanding.league_rank")
    leagueL10Rank = fields.Integer(attribute="StatsapiStanding.leaguel_10_rank")
    leagueHomeRank = fields.Integer(attribute="StatsapiStanding.league_home_rank")
    leagueRoadRank = fields.Integer(attribute="StatsapiStanding.league_road_rank")
    points = fields.Integer(attribute="StatsapiStanding.points")
    pointsPercentage = fields.Float(attribute="StatsapiStanding.points_percentage")
    ppConferenceRank = fields.Integer(attribute="StatsapiStanding.pp_conference_rank")
    ppDivisionRank = fields.Integer(attribute="StatsapiStanding.pp_division_rank")
    ppLeagueRank = fields.Integer(attribute="StatsapiStanding.pp_league_rank")
    regulationWins = fields.Integer(attribute="StatsapiStanding.regulation_wins")
    row = fields.Integer(attribute="StatsapiStanding.row")
    streak = fields.Str(attribute="StatsapiStanding.streak")
    teamId = fields.Integer(attribute="StatsapiStanding.team_id")
    teamName = fields.Str(attribute="team_name")
    wildCardRank = fields.Integer(attribute="StatsapiStanding.wild_card_rank")
