""" hits endpoints for statsapi and parses data into database """
import requests
from typing import Any, List, Dict, Optional
from models.utils import BASE, get_session
from models.statsapi.player import StatsapiPlayer
from models.statsapi.standing import StatsapiStanding
from models.statsapi.team import StatsapiTeam
from uploader.schemas.statsapi.player_schema import RawPlayer, Player
from uploader.schemas.statsapi.standings_schema import RawStanding, Standing
from uploader.schemas.statsapi.team_schema import RawTeam, Team

###########
# Extract #
###########

BASE_URL = "https://statsapi.web.nhl.com/api/v1"

def extract_statsapi_data(endpoint: str) -> List:
    """ gets data from statsapi endopint and returns """
    url = f"{BASE_URL}{endpoint}"
    response = requests.get(url)
    if response.ok:
        return response.json()
    
    # TODO: handle elegantly
    return None

########
# Load #
########

def load_data(session: Any, model: Any, data: List, commit_every_n: Optional[int] = 50) -> None:
    """ insert data to database """
    BASE.metadata.create_all(tables=[model.__table__], checkfirst=True)
    for index, row in enumerate(data, start=1):
        if index % commit_every_n == 0:
            # TODO: log this with a real logger
            print(f"Inserted {index}/{len(data)} rows into {model.__tablename__}")
            session.commit()

        to_merge = model(**row)
        session.merge(to_merge)
    session.commit()
    print(f"Inserted {len(data)}/{len(data)} rows into {model.__tablename__}")


#############
# Standings #
#############

def upload_team_data(session: Any) -> List[Dict]:
    """ ulpoads team data and returns parsed values """
    raw_data = extract_statsapi_data("/teams")
    validated_data = RawTeam().load(raw_data["teams"], many=True)
    parsed_data = Team().dump(validated_data, many=True)
    load_data(session, StatsapiTeam, parsed_data)
    return parsed_data


def upload_standing_data(session: Any) -> List[Dict]:
    """ uploads standings data and returns parsed values """
    raw_data = extract_statsapi_data("/standings")
    validated_data = RawStanding().load(raw_data)
    parsed_data = []
    for division in validated_data.get("records", []):
        for team in division.get("teamRecords", []):
            parsed_data.append(Standing().dump(team))
     
    load_data(session, StatsapiStanding, parsed_data)


def upload_players_for_team(session: Any, team_id: int) -> None:
    """ pull a team's roster, then upload all the players """
    roster = extract_statsapi_data(f"/teams/{team_id}?expand=team.roster")
    raw_data = []
    for player_node in roster["teams"][0]["roster"]["roster"]:
        raw_data.append(extract_statsapi_data(f"/people/{player_node['person']['id']}")["people"][0])
    
    validated_data = RawPlayer().load(raw_data, many=True)
    parsed_data = Player().dump(validated_data, many=True)
    load_data(session, StatsapiPlayer, parsed_data)


##################
# Overall upload #
##################

def upload_statsapi_data(session: Any):
    """ uploads all statsapi data -- by pulling standings --> teams --> players """
    teams = upload_team_data(session)
    upload_standing_data(session)
    for team in teams:
        upload_players_for_team(session, team["id"])


def main():
    """ main func """
    session = get_session()
    upload_statsapi_data(session)


if __name__ == "__main__":
    main()
