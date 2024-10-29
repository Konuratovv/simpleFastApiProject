import uvicorn

PORT = 8000
HOST = "127.0.0.1"
APP_NAME = "app.main:app"

if __name__ == "__main__":
    uvicorn.run(app=APP_NAME, host=HOST, port=PORT, reload=True)