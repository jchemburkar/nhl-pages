""" api endpoints for team page """
import time
from flask import Blueprint, jsonify
from api.utils import SESSION
from api.team.schemas import TeamSchema
from models.statsapi.team import StatsapiTeam

TEAM_API = Blueprint("teams", __name__)

@TEAM_API.route("/teams/<int:team_id>", methods=["GET"])
def get_team(team_id: int):
    """ gets a specific team by id """
    team = SESSION.query(StatsapiTeam).filter(StatsapiTeam.id == team_id).first()
    team_dumped = TeamSchema().dump(team)
    return jsonify(team_dumped)


@TEAM_API.route("/teams", methods=["GET"])
def get_all_teams():
    """ gets all teams """
    teams = SESSION.query(StatsapiTeam).all()
    teams_dumped = TeamSchema().dump(teams, many=True)
    return jsonify(teams_dumped)
