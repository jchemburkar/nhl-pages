from flask import Flask
from api.player.blueprints import PLAYER_API

APP = Flask(__name__)

# register any blueprints with the base api
for blueprint in [PLAYER_API]:
    APP.register_blueprint(blueprint)


if __name__ == '__main__':
    APP.run(host='0.0.0.0')
