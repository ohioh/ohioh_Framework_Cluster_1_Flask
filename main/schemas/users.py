from datetime import datetime

from marshmallow import Schema, EXCLUDE
import marshmallow.fields as ms_fields


class UserSchema(Schema):
    user_id = ms_fields.Str(required=True)
    user_timestemp = ms_fields.DateTime(default=datetime.now(), required=True)
    user_mac = ms_fields.Str(required=False)
    first_name = ms_fields.Str(required=False)
    last_name = ms_fields.Str(required=False)
    age = ms_fields.Int(required=False)
    country=ms_fields.Str(required=False)
    is_infected = ms_fields.Bool(required=True)
    infection_accuracy = ms_fields.Float(required=True)
    user_privacy_data = ms_fields.Bool(required=True)
    tracking_save_duration = ms_fields.Float(required=True)
    bluetooth_save_duration = ms_fields.Float(required=True)
    data_save_duration = ms_fields.Float(required=True)
    phone = ms_fields.Int(required=False)
    zip_code = ms_fields.Int(required=False)
    registration_date = ms_fields.Date(default=datetime.now().date(), required=False)

    class Meta:
        unknown = EXCLUDE


