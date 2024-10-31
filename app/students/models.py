from datetime import datetime, date
from app.db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, ForeignKey


class Student(Base):
    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    first_name: Mapped[str] = mapped_column(String(150), nullable=False)
    second_name: Mapped[str] = mapped_column(String(150), nullable=False)
    address: Mapped[str] = mapped_column(Text)
    phone_number: Mapped[str] = mapped_column(unique=True, nullable=False)
    date_of_birth: Mapped[date]
    major_id: Mapped[int] = mapped_column(ForeignKey('majors.id'), nullable=True)
    
    major: Mapped["Major"] = relationship("Major", back_populates="students")
    
    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}(id = {self.id})",
            f"first_name = {self.first_name}",
            f"second_name = {self.second_name}",
        )
        
    def __repr__(self):
        return str(self)
    

class Major(Base):
    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    major_name: Mapped[str] = mapped_column(String(150))
    major_description: Mapped[str] = mapped_column(Text, nullable=True)
    count_students: Mapped[int] = mapped_column(server_default='0')
    
    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, major_name={self.major_name!r})"

    def __repr__(self):
        return str(self)
    