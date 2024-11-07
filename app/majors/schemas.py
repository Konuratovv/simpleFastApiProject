from pydantic import BaseModel, Field


class SMajorsGet(BaseModel):
    id: int
    major_name: str = Field(..., description='Название факультета')
    major_description: str = Field(default=None, description="Описание факультета")
    count_students: int = Field(0, description="Количество студентов")
    

class SMajorAdd(BaseModel):
    major_name: str = Field(..., description='Название факультета')
    major_description: str = Field(default=None, description="Описание факультета")
    count_students: int = Field(0, description="Количество студентов")