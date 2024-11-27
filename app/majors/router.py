from fastapi import APIRouter, status, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.majors.schemas import SMajorAdd, SMajorsGet
from app.majors.services import MajorService
from app.db.database import get_session

router = APIRouter(prefix='/majors', tags=['Working with majors'])

@router.post('/add/', status_code=status.HTTP_201_CREATED)
async def create_major(major: SMajorAdd, session: AsyncSession = Depends(get_session)) -> dict:
    return await MajorService.create(session, **major.model_dump())
        
@router.get('/', status_code=status.HTTP_200_OK)
async def get_majors(session: AsyncSession = Depends(get_session)):
    return await MajorService.get_all(session)
    
@router.get('/{id}/', status_code=status.HTTP_200_OK)
async def get_major_by_id(id:int, session: AsyncSession = Depends(get_session)):
    return await MajorService.get_by_id(id, session)
            