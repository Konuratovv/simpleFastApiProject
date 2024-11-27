from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text
from app.base.models import Base
from app.students.models import Student


class Major(Base):
    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    major_name: Mapped[str] = mapped_column(String(150))
    major_description: Mapped[str] = mapped_column(Text, nullable=True)
    count_students: Mapped[int] = mapped_column(server_default='0')
    students: Mapped[list["Student"]] = relationship("Student", back_populates="major")

        
    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, major_name={self.major_name!r})"

    def __repr__(self):
        return str(self)