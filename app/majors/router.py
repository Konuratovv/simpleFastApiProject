from fastapi import APIRouter, status

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from app.majors.schemas import SMajorAdd, SMajorsGet
from app.majors.models import Major
from app.db.database import async_session_maker

router = APIRouter(prefix='/majors', tags=['Working with majors'])

@router.post('/add/', status_code=status.HTTP_201_CREATED)
async def create_major(major: SMajorAdd) -> dict:
    async with async_session_maker() as session:
        async with session.begin():
            new_instance = Major(**major.model_dump())
            session.add(new_instance)
            try:
                await session.commit()
            except SQLAlchemyError as e:
                await session.rollback()
                raise e
            return {"message": "success"}
        
@router.get('/', status_code=status.HTTP_200_OK)
async def get_majors():
    async with async_session_maker() as session:
        query = select(Major)
        majors = await session.execute(query)
        return majors.scalars().all()

            