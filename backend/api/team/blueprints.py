""" api endpoints for team page """
import time
from flask import Blueprint, jsonify
from api.utils import SESSION
from api.team.schemas import TeamSchema
from models.statsapi.team import StatsapiTeam

TEAM_API = Blueprint("teams", __name__)

@TEAM_API.route("/teams/<int:team_id>", methods=["GET"])
def get_team(team_id: int):
    team = SESSION.query(StatsapiTeam).filter(StatsapiPTeam.id == team_id).first()
    team_dumped = TeamSchema().dump(team)
    return jsonify(team_dumped)
