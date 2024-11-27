from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

PRODUCTION = False

if PRODUCTION:
    from .prod import get_db_url
else:
    from .dev import get_db_url
    
db_url = get_db_url()
db_engine = create_async_engine(db_url)
async_session_maker = async_sessionmaker(db_engine, class_=AsyncSession, expire_on_commit=True)

async def get_session() -> AsyncSession:
    async with async_session_maker() as session:
        yield session