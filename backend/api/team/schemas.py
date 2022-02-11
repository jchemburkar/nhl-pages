""" parses output of query into dict for FE """
from marshmallow import Schema, fields

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
    shortName = fields.Str(attribute="short_name")
    teamName = fields.Str(attribute="team_name")
    venueId = fields.Integer(attribute="venue_id")
    venueName = fields.Str(attribute="venueNname")
