""" models teams api reponse and team db rows """
from marshmallow import Schema, fields
from uploader.schemas.shared import RawInfo, RawPosition

##############
# Raw Schema #
##############

class RawTeamVenueTimezone(Schema):
    id = fields.Str()
    offset = fields.Integer()
    tz = fields.Str()


class RawTeamVenue(Schema):
    city = fields.Str()
    id = fields.Integer()
    link = fields.Str()
    name = fields.Str()
    timeZone = fields.Nested(RawTeamVenueTimezone)


class RawTeamFranchise(Schema):
    franchiseId = fields.Integer()
    link = fields.Str()
    teamName = fields.Str()


class RawTeam(Schema):
    abbreviation = fields.Str()
    active = fields.Boolean()
    conference = fields.Nested(RawInfo)
    division = fields.Nested(RawInfo)
    firstYearOfPlay = fields.Str()
    franchise = fields.Nested(RawTeamFranchise)
    franchiseId = fields.Integer()
    id = fields.Integer()
    link = fields.Str()
    locationName = fields.Str()
    name = fields.Str()
    officialSiteUrl = fields.Str()
    shortName = fields.Str()
    teamName = fields.Str()
    venue = fields.Nested(RawTeamVenue)


#################
# Parsed Schema #
#################

class Team(Schema):
    abbreviation = fields.Str()
    active = fields.Boolean()
    conference_id = fields.Integer(attribute="conference.id")
    conference_name = fields.Str(attribute="conference.name")
    division_id = fields.Integer(attribute="division.id")
    division_name = fields.Str(attribute="division.name")
    first_year_of_play = fields.Integer(attribute="firstYearOfPlay")
    franchise_id = fields.Integer(attribute="franchiseId")
    id = fields.Integer()
    link = fields.Str()
    location_name = fields.Str(attribute="locationName")
    name = fields.Str()
    official_site_url = fields.Str(attribute="officialSiteUrl")
    short_name = fields.Str(attribute="shortName")
    team_name = fields.Str(attribute="teamName")
    venue_id = fields.Integer(attribute="venue.id")
    venue_name = fields.Str(attribute="venue.name")