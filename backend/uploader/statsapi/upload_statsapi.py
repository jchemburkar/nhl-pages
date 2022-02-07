""" hits endpoints for statsapi and parses data into database """
import requests
from typing import Any, List, Dict, Optional
from models.utils import BASE, get_session
from models.statsapi.player import StatsapiPlayer
from uploader.schemas.player_schema import RawPlayer, Player

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


#############
# Transform #
#############

def transform_data(raw_data: Any, raw_schema: Any, parsed_schema: Any) -> List[Dict]:
    """ takes in raw data from api and turns into a row to be loaded """
    if not isinstance(raw_data, (dict, list)):
        # TODO: add logging here
        pass

    raw_data_is_list = isinstance(raw_data, list)
    validated_data = raw_schema().load(raw_data, many=raw_data_is_list)
    parsed_data = parsed_schema().dump(validated_data, many=raw_data_is_list)
    if not raw_data_is_list:
        parsed_data = [parsed_data]

    return parsed_data


########
# Load #
########

def load_data(session: Any, model: Any, data: List, commit_every_n: Optional[int] = 25) -> None:
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


##################
# Overall upload #
##################

def main():
    """ main func """
    session = get_session()
    raw_data = extract_statsapi_data("/people/8470638")
    data = transform_data(raw_data["people"], RawPlayer, Player)
    load_data(session, StatsapiPlayer, data)


if __name__ == "__main__":
    main()
