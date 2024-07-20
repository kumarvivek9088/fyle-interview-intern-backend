from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment
from core.models.users import User
from core.models.teachers import Teacher

from .schema import TeacherSchema
principal_resources = Blueprint('principal_resources', __name__)

@principal_resources.route('/teachers',methods = ["GET"],strict_slashes=False)
@decorators.authenticate_principal
def list_assignments(p):
    """Returns list of teachers"""
    teachers = Teacher.query.all()
    teachers_dump = TeacherSchema().dump(teachers,many=True)
    return APIResponse.respond(data=teachers_dump)
