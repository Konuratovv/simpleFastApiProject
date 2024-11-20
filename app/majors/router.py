from fastapi import APIRouter, status

from app.majors.schemas import SMajorAdd, SMajorsGet
from app.majors.services import MajorService

router = APIRouter(prefix='/majors', tags=['Working with majors'])

@router.post('/add/', status_code=status.HTTP_201_CREATED)
async def create_major(major: SMajorAdd) -> dict:
    return await MajorService.create(**major.model_dump())
        
@router.get('/', status_code=status.HTTP_200_OK)
async def get_majors() -> SMajorsGet:
    return await MajorService.get_all()
    
@router.get('/{id}/', status_code=status.HTTP_200_OK)
async def get_major_by_id(id:int):
    return await MajorService.get_by_id(id)
            