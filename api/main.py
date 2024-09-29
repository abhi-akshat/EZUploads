from fastapi import FastAPI
from routes.admin import router as admin_router
from routes.client import router as client_router
from fastapi.middleware.cors import CORSMiddleware
from db.database import engine, get_db
from init_db import create_admin_user
import os

from db.models import Base
Base.metadata.create_all(bind=engine)

db = next(get_db())
create_admin_user(db)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(admin_router, prefix="/admin", tags=["Admin"])
app.include_router(client_router, tags=["Client"])


from db.models import Base
Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"message": "Welcome to EZUploads API!"}

# def get_uploaded_file(filename: str):
#     file_path = os.path.join("uploads", filename)
#     if not os.path.exists(file_path):
#         return {"message": "File not found"}
#     return {"file_path": file_path}