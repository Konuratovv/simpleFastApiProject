import os
from enum import Enum
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel, Field, EmailStr
from datetime import date, datetime


class Major(str, Enum):
    informatics = "Информатика"
    economics = "Экономика"
    law = "Право"
    medicine = "Медицина"
    engineering = "Инженерия"
    languages = "Языки"


class Student(BaseModel):
    student_id: int
    phone_number: str = Field(description="Номер телефона в международном формате, начинающийся с '+'")
    first_name: str = Field(min_length=1, max_length=50, description="Имя студента, от 1 до 50 символов")
    last_name: str = Field(min_length=1, max_length=50, description="Фамилия студента, от 1 до 50 символов")
    date_of_birth: date = Field(description="Дата рождения студента в формате ГГГГ-ММ-ДД")
    email: EmailStr = Field(description="Электронная почта студента")
    address: str = Field(min_length=10, max_length=200, description="Адрес студента, не более 200 символов")
    enrollment_year: int = Field(ge=2002, description="Год поступления должен быть не меньше 2002")
    major: Major = Field(description="Специальность студента")
    course: int = Field(ge=1, le=5, description="Курс должен быть в диапазоне от 1 до 5")
    special_notes: Optional[str] = Field(default=None, max_length=500,
                                         description="Дополнительные заметки, не более 500 символов")

app = FastAPI()

path_to_json = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data.json')

@app.get('/')
def home_page():
    return {'message': 'Hi, FastAPI!'}

# @app.get('/students')
# def get_all_students() -> Student:
#     return json_to_dict_list(path_to_json)

# @app.get('/students/{student_id}')
# def get_one_student(student_id: int) -> Student:
#     students = json_to_dict_list(path_to_json)
#     for student in students:
#         if student["student_id"] == student_id:
#             student_dict = student
#     return student_dict

 