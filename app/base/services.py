from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

class BaseService:
    model = None
    session_maker = None
    
    @classmethod
    async def get_all(cls):
        async with cls.session_maker as session:
            query = select(cls.model)
            result = await session.execute(query)
            return result.scalars().all()
        
    @classmethod
    async def get_by_id(cls, id):
        async with cls.session_maker as session:
            return await session.get(cls.model, id)
        
    @classmethod
    async def create(cls, **values):
        async with cls.session_maker as session:
            async with session.begin():
                new_instance = cls.model(**values)
                try:
                    session.add(new_instance)
                    session.commit()
                except SQLAlchemyError as e:
                    session.rollback()
                    raise e
                return {'message': 'created successfuly!'}
            