""" models player api reponse and player db rows """
from marshmallow import Schema, fields, pre_dump
from uploader.schemas.shared import RawInfo, RawPosition

##############
# Raw Schema #
##############

class RawPlayer(Schema):
    active = fields.Boolean()
    alternateCaptain = fields.Boolean()
    birthCity = fields.Str()
    birthCountry = fields.Str()
    birthDate = fields.Str()
    birthStateProvince = fields.Str()
    captain = fields.Boolean()
    currentAge = fields.Integer()
    currentTeam = fields.Nested(RawInfo)
    firstName = fields.Str()
    fullName = fields.Str()
    height = fields.Str()
    id = fields.Integer()
    lastName = fields.Str()
    link = fields.Str()
    nationality = fields.Str()
    primaryNumber = fields.Str()
    primaryPosition = fields.Nested(RawPosition)
    rookie = fields.Boolean()
    rosterStatus = fields.Str()
    shootsCatches = fields.Str()
    weight = fields.Integer()


#################
# Parsed Schema #
#################

class Player(Schema):
    birth_city = fields.Str(attribute="birthCity")
    birth_country = fields.Str(attribute="birthCountry")
    birth_date = fields.Str(attribute="birthDate")
    birth_state_province = fields.Str(attribute="birthStateProvince")
    current_age = fields.Integer(attribute="currentAge")
    current_team_id = fields.Integer(attribute="currentTeam.id")
    first_name = fields.Str(attribute="firstName")
    full_name = fields.Str(attribute="fullName")
    height = fields.Str()
    id = fields.Integer()
    is_active = fields.Boolean(attribute="active")
    is_alternate_captain = fields.Boolean(attribute="alternateCaptain")
    is_captain = fields.Boolean(attribute="captain")
    is_rookie = fields.Boolean(attribute="rookie")
    last_name = fields.Str(attribute="lastName")
    link = fields.Str()
    nationality = fields.Str()
    primary_number = fields.Str(attribute="primaryNumber")
    primary_position = fields.Str(attribute="primaryPosition.code")
    roster_status = fields.Str(attribute="rosterStatus")
    shoots_catches = fields.Str(attribute="shootsCatches")
    weight = fields.Integer()

    @pre_dump
    def predump(self, data, **kwargs):
        """ sets height to be inches """
        height = data["height"].split("\'")
        data["height"] = 12 * int(height[0]) + int(height[1].replace('"', ''))
        return data
