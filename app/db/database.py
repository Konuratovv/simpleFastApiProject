from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

PRODUCTION = False

if PRODUCTION:
    from .prod import get_db_url
else:
    from .dev import get_db_url
    
db_url = get_db_url()
db_engine = create_async_engine(db_url)
async_session_maker = async_sessionmaker(db_engine, expire_on_commit=True)
    
    