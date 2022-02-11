''' sql alchemy model for statsapi_standing table '''
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import VARCHAR, TINYINT, SMALLINT, MEDIUMINT, DECIMAL, INTEGER, DATETIME
from models.utils import BASE, DATABASE
from models.statsapi.team import StatsapiTeam


class StatsapiStanding(BASE):

    __tablename__ = 'statsapi_standing'
    __table_args__ = {"schema": DATABASE}

    team_id = Column(StatsapiTeam.id.type, ForeignKey(StatsapiTeam.id), primary_key=True)
    league_id = Column(MEDIUMINT)
    games_played = Column(TINYINT)
    regulation_wins = Column(TINYINT)
    row = Column(TINYINT)
    streak = Column(VARCHAR(5))
    points = Column(TINYINT)
    points_percentage = Column(DECIMAL(5,4))
    goals_for = Column(SMALLINT)
    goals_against = Column(SMALLINT)
    conference_rank = Column(TINYINT)
    conference_l10_rank = Column(TINYINT)
    conference_home_rank = Column(TINYINT)
    conference_road_rank = Column(TINYINT)
    division_home_rank = Column(TINYINT)
    division_l10_rank = Column(TINYINT)
    division_rank = Column(TINYINT)
    division_road_rank = Column(TINYINT)
    league_rank = Column(TINYINT)
    league_l10_rank = Column(TINYINT)
    league_home_rank = Column(TINYINT)
    league_road_rank = Column(TINYINT)
    pp_conference_rank = Column(TINYINT)
    pp_division_rank = Column(TINYINT)
    pp_league_rank = Column(TINYINT)
    wild_card_rank = Column(TINYINT)
    last_updated = Column(DATETIME)
