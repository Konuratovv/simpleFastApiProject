from app.base.services import BaseService
from app.students.models import Student


class StudentService(BaseService):
    model = Student