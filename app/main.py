import os
from fastapi import FastAPI

from app.majors.router import router as major_router

app = FastAPI()

path_to_json = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data.json')

@app.get('/')
def home_page():
    return {'message': 'Hi, FastAPI!'}

app.include_router(major_router)


 