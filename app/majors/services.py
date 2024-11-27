from app.base.services import BaseService
from app.majors.models import Major
from app.db.database import async_session_maker

class MajorService(BaseService):
    model = Major