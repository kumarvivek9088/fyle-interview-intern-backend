from marshmallow import Schema, EXCLUDE, fields, post_load
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow_enum import EnumField
from core.models.teachers import Teacher
from core.libs.helpers import GeneralObject
from core.models.users import User

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        unknown = EXCLUDE

    id = auto_field(required=True,allow_none=False)
    username = auto_field(dump_only=True)
    email = auto_field(dump_only=True)

class TeacherSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Teacher
        unknown = EXCLUDE

    
    id = auto_field(required=True,allow_none=False)
    # user = fields.Nested(UserSchema,dump_only= True)
    user_id = auto_field(dump_only=True)
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only = True)

    @post_load
    def initiate_class(self,data_dict,many,partial):
        return Teacher(**data_dict)