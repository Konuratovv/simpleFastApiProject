from datetime import datetime
from sqlalchemy.ext.asyncio import create_async_engine, AsyncAttrs, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column
from sqlalchemy import func

PRODUCTION = False

if PRODUCTION:
    from .prod import get_db_url
else:
    from .dev import get_db_url
    
db_url = get_db_url()
db_engine = create_async_engine(db_url)
async_session_maker = async_sessionmaker(db_engine, expire_on_commit=True)


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True
    
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=datetime.now)
    
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"
    
    