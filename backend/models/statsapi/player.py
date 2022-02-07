''' sql alchemy model for statsapi_player table '''
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import VARCHAR, TINYINT, MEDIUMINT, DATE
from models.utils import BASE


class StatsapiPlayer(BASE):
    __tablename__ = 'statsapi_player'

    id = Column(MEDIUMINT, primary_key=True)
    first_name = Column(VARCHAR(30))
    last_name = Column(VARCHAR(30))
    fullName = Column(VARCHAR(100))
    current_team_id = Column(MEDIUMINT)
    birth_date = Column(DATE)
    birth_city = Column(VARCHAR(30))
    birth_country = Column(VARCHAR(30))
    birth_state_province = Column(VARCHAR(30))
    height = Column(TINYINT)
    weight = Column(TINYINT)
    current_age = Column(TINYINT)
    is_active = Column(TINYINT(1))
    is_alternate_captain = Column(TINYINT(1))
    is_captain = Column(TINYINT(1))
    is_rookie = Column(TINYINT(1))
    link = Column(VARCHAR(100))
    nationality = Column(VARCHAR(30))
    primary_number = Column(TINYINT)
    primary_position = Column(VARCHAR(5))
    roster_status = Column(VARCHAR(5))
    shoots_catches = Column(VARCHAR(5))
