from datetime import date
from pydantic import BaseModel, Field


class SStudent(BaseModel):
    id: int
    first_name: str = Field(..., min_length=1, max_length=50, description="Имя студента, от 1 до 50 символов")
    second_name: str = Field(..., min_length=1, max_length=50, description="Фамилия студента, от 1 до 50 символов")
    address: str = Field(..., min_length=10, max_length=200, description="Адрес студента, не более 200 символов")
    phone_number: str = Field(..., description="Номер телефона в международном формате, начинающийся с '+'")
    date_of_birth: date = Field(..., description="Дата рождения студента в формате ГГГГ-ММ-ДД")
    major_id: int = Field(..., ge=1, description="ID специальности студента")
    
class SStudentAdd(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=50, description="Имя студента, от 1 до 50 символов")
    second_name: str = Field(..., min_length=1, max_length=50, description="Фамилия студента, от 1 до 50 символов")
    address: str = Field(..., min_length=10, max_length=200, description="Адрес студента, не более 200 символов")
    phone_number: str = Field(..., description="Номер телефона в международном формате, начинающийся с '+'")
    date_of_birth: date = Field(..., description="Дата рождения студента в формате ГГГГ-ММ-ДД")
    major_id: int = Field(..., ge=1, description="ID специальности студента")