from datetime import datetime, date, timedelta

from marshmallow import Schema, EXCLUDE
import marshmallow.fields as ms_fields


class UserSchema(Schema):
    user_id = ms_fields.Str()
    user_timestamp = ms_fields.DateTime(default=datetime.now())
    user_mac = ms_fields.Str(default="")
    first_name = ms_fields.Str(default="")
    last_name = ms_fields.Str(default="")
    age = ms_fields.Int(required=False, default="")
    country=ms_fields.Str(required=False, default="")
    is_infected = ms_fields.Bool(default=False)
    infection_accuracy = ms_fields.Float(default=0.0)
    user_privacy_data = ms_fields.Bool(default=False)
    tracking_save_duration = ms_fields.Int(default=14)
    bluetooth_save_duration = ms_fields.Int(default=14)
    data_save_duration = ms_fields.Int(default=90)
    data_delete_date = ms_fields.Date()
    phone = ms_fields.Int(required=False)
    zip_code = ms_fields.Int(required=False)
    registration_date = ms_fields.Date(default=date.today())


    class Meta:
        unknown = EXCLUDE


