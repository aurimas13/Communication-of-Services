from marshmallow import Schema, fields


Get = Schema.from_dict({"event_type": fields.Str(), "event_payload": fields.Str()})


class Event(Schema):
    event_type = fields.Str(required=True)
    event_payload = fields.Str(required=True)

# event_data = {
# 	    "event_type":"user_left",
# 	    "event_payload":"Thomas"
# }