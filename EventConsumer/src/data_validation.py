from marshmallow import Schema, fields


class Event(Schema):
    event_type = fields.Str(required=True)
    event_payload = fields.Str(required=True)