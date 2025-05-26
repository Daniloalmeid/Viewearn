from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str()
    email = fields.Email()
    is_creator = fields.Bool()
    created_at = fields.DateTime()

class VideoSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    youtube_id = fields.Str()
    creator_id = fields.Int()
    created_at = fields.DateTime()

class ViewSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int()
    video_id = fields.Int()
    watched_seconds = fields.Int()
    rewarded = fields.Bool()
    viewed_at = fields.DateTime()
