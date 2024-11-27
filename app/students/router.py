from fastapi import APIRouter, status, Depends

from app.students.schemas import SStudentAdd, SStudent
from app.db.database import get_session
from app.students.services import StudentService

from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix='/students', tags=['Working with students'])


@router.post('/add/', status_code=status.HTTP_201_CREATED)
async def add_student(student: SStudentAdd, session: AsyncSession = Depends(get_session)):
    return await StudentService.create(session, **student.model_dump())

@router.get('/', status_code=status.HTTP_200_OK)
async def students(session: AsyncSession = Depends(get_session)):
    return await StudentService.get_all(session)
    