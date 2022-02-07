""" models player api reponse and player db rows """
from marshmallow import Schema, fields

class RawPosition(Schema):
    abbreviation = fields.Str()
    code = fields.Str()
    name = fields.Str()
    type = fields.Str()

class RawInfo(Schema):
    id = fields.Integer()
    link = fields.Str()
    name = fields.Str()
    