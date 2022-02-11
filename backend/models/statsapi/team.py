''' sql alchemy model for statsapi_team table '''
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import VARCHAR, TINYINT, MEDIUMINT
from models.utils import BASE, DATABASE


class StatsapiTeam(BASE):

    __tablename__ = 'statsapi_team'
    __table_args__ = {"schema": DATABASE}

    id = Column(MEDIUMINT, primary_key=True)
    name = Column(VARCHAR(50))
    team_name = Column(VARCHAR(20))
    short_name = Column(VARCHAR(20))
    abbreviation = Column(VARCHAR(5))
    active = Column(TINYINT)
    venue_id = Column(MEDIUMINT)
    venue_name = Column(VARCHAR(50))
    location_name = Column(VARCHAR(50))
    conference_id = Column(MEDIUMINT)
    conference_name = Column(VARCHAR(50))
    division_id = Column(MEDIUMINT)
    division_name = Column(VARCHAR(50))
    first_year_of_play = Column(MEDIUMINT)
    franchise_id = Column(MEDIUMINT)
    link = Column(VARCHAR(50))
    official_site_url = Column(VARCHAR(50))
