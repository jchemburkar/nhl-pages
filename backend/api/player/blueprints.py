""" api endpoints for player page """
import time
from flask import Blueprint, jsonify
from api.utils import SESSION
from api.player.schemas import PlayerSchema
from models.statsapi.player import StatsapiPlayer

PLAYER_API = Blueprint("players", __name__)

@PLAYER_API.route("/players/<int:player_id>", methods=["GET"])
def get_current_time(player_id):
    player = SESSION.query(StatsapiPlayer).filter(StatsapiPlayer.id == player_id).first()
    player_dumped = PlayerSchema().dump(player)
    return jsonify(player_dumped)
