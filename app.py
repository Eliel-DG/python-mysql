from fastapi import FastAPI
from routes.alumno import router
app = FastAPI()
app.include_router(router)
