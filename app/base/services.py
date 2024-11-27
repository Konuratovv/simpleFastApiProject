from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

class BaseService:
    model = None
    
    @classmethod
    async def get_all(cls, session: AsyncSession):
        query = select(cls.model)
        result = await session.execute(query)
        return result.scalars().all()
        
    @classmethod
    async def get_by_id(cls, id, session: AsyncSession):
        return await session.get(cls.model, id)
        
    @classmethod
    async def create(cls, session: AsyncSession, **values):
        async with session.begin():
            new_instance = cls.model(**values)
            try:
                session.add(new_instance)
                session.commit()
            except SQLAlchemyError as e:
                session.rollback()
                raise e
            return {'message': 'created successfuly!'}
        