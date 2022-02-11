""" api endpoints for standings page """
import time
from flask import Blueprint, jsonify
from api.utils import SESSION
from api.standings.schemas import StandingSchema
from models.statsapi.standing import StatsapiStanding

STATSAPI_API = Blueprint("statsapi", __name__)

@STATSAPI_API.route("/standings", methods=["GET"])
def get_standings():
    standings = SESSION.query(StatsapiStanding).all()
    standings_dumped = StandingSchema().dump(standings, many=True)
    return jsonify(standings_dumped)
