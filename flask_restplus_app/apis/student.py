"""
Contains API's related to Student
"""
import traceback

from flask_restplus import Namespace
from flask_restplus import Resource
from flask_restplus import fields

from flask_restplus_app.services.common import token_required
from flask_restplus_app.services.student_services import add_student
from flask_restplus_app.services.student_services import get_student

api = Namespace("student", description="Operations related to student")

student_model = api.model(
    "Student",
    {
        "id": fields.Integer,
        "name": fields.String(description="student name", min_length=3, required=True),
    },
)


@api.route("/")
class StudentAPI(Resource):
    """
    Get all students and insert a new student
    """

    parser = api.parser()
    parser.add_argument(
        "name",
        type=str,
        required=True,
        help="student name cannot be blank!",
        location="json",
    )

    @api.response(500, "Error in getting students")
    @api.marshal_list_with(student_model)
    def get(self):
        """
        Get all the students from DB
        """
        try:
            students = []  # get_students()
            return students
        except Exception:
            traceback.print_exc()
            api.abort(500, "Error in getting students")

    @api.response(409, "Student already exists")
    @api.response(201, "Student successfully added.")
    @api.response(500, "Error in adding a student")
    @api.expect(student_model, validate=True)
    @token_required
    @api.doc(security="apikey")
    def post(self):
        """
        Insert a new student
        """
        args = self.parser.parse_args(strict=True)
        student_name = args["name"].strip()

        student = add_student(student_name)
        if student:
            return api.marshal(student, student_model), 201
        else:
            api.abort(409, "Student alreday exists")


@api.route("/<string:name>")
@api.param("name", "student name")
class StudentCheckAPI(Resource):
    """
    Get the student object when student name is supplied
    """

    @api.response(404, "Student not found")
    @api.response(500, "Error in getting student")
    @api.marshal_with(student_model)
    def get(self, name):
        """
        Returns the student object for the supplied student name
        """
        student = get_student(name)
        if student:
            return student
        else:
            api.abort(404, "Student not found")
