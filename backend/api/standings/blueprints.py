""" api endpoints for standings page """
import time
from flask import Blueprint, jsonify
from api.utils import SESSION
from api.standings.schemas import StandingSchema
from models.statsapi.standing import StatsapiStanding
from models.statsapi.team import StatsapiTeam

STATSAPI_API = Blueprint("statsapi", __name__)

@STATSAPI_API.route("/standings", methods=["GET"])
def get_standings():
    standings = (
        SESSION.query(
            StatsapiStanding,
            StatsapiTeam.conference_id,
            StatsapiTeam.conference_name,
            StatsapiTeam.division_id,
            StatsapiTeam.division_name,
            StatsapiTeam.team_name,
        )
        .join(StatsapiTeam)
        .all()
    )
    standings_dumped = StandingSchema().dump(standings, many=True)
    return jsonify(standings_dumped)
