import os
from fastapi import FastAPI

from app.majors.router import router as major_router
from app.students.router import router as student_router

app = FastAPI()

path_to_json = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data.json')

@app.get('/')
def home_page():
    return {'message': 'Hi, FastAPI!'}

app.include_router(major_router)
app.include_router(student_router)

