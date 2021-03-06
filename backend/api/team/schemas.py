""" parses output of query into dict for FE """
from marshmallow import Schema, fields, pre_dump

class PlayerSchema(Schema):
    id = fields.Integer()
    firstName = fields.Str(attribute="first_name")
    lastName = fields.Str(attribute="last_name")
    fullName = fields.Str(attribute="full_name")
    currentTeamId = fields.Integer(attribute="current_team_id")
    birthDate = fields.Str(attribute="birth_date")
    birthCity = fields.Str(attribute="birth_city")
    birthCountry = fields.Str(attribute="birth_country")
    birthStateProvince = fields.Str(attribute="birth_state_province")
    height = fields.Integer()
    weight = fields.Integer()
    currentAge = fields.Integer(attribute="current_age")
    isActive = fields.Integer(attribute="is_active")
    isAlternate_captain = fields.Integer(attribute="is_alternate_captain")
    isCaptain = fields.Integer(attribute="is_captain")
    isRookie = fields.Integer(attribute="is_rookie")
    link = fields.Str()
    nationality = fields.Str()
    primaryNumber = fields.Integer(attribute="primary_number")
    primaryPosition = fields.Str(attribute="primary_position")
    rosterStatus = fields.Str(attribute="roster_status")
    shootsCatches = fields.Str(attribute="shoots_catches")


class TeamSchema(Schema):
    abbreviation = fields.Str()
    active = fields.Boolean()
    conferenceId = fields.Integer(attribute="conference_id")
    conferenceName = fields.Str(attribute="conference_name")
    divisionId = fields.Integer(attribute="division_id")
    divisionName = fields.Str(attribute="division_name")
    firstYearOfPlay = fields.Integer(attribute="first_year_of_play")
    franchiseId = fields.Integer(attribute="franchise_id")
    id = fields.Integer()
    link = fields.Str()
    locationName = fields.Str(attribute="location_name")
    name = fields.Str()
    officialSiteUrl = fields.Str(attribute="official_site_url")
    players = fields.Nested(PlayerSchema(), many=True)
    shortName = fields.Str(attribute="short_name")
    teamName = fields.Str(attribute="team_name")
    venueId = fields.Integer(attribute="venue_id")
    venueName = fields.Str(attribute="venue_name")

    @pre_dump
    def predump_players(self, data, **kwargs):
        """ filter for active only """
        data.players = [x for x in data.players if x.is_active]
        return data
