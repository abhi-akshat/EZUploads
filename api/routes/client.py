from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from utils import hash_password, create_access_token, get_file_download_link, verify_password
from db.database import get_db
from db.models import User
import aws
import os
import uuid
from pydantic import BaseModel

router = APIRouter()

class SignupRequest(BaseModel):
    username: str
    password: str

@router.post("/signup")
async def signup(signup_request: SignupRequest, db: Session = Depends(get_db)):

    existing_user = db.query(User).filter(User.username == signup_request.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    hashed_password = hash_password(signup_request.password)
    user_id = str(uuid.uuid4())
    new_user = User(id=user_id, username=signup_request.username, password=hashed_password, user_type="client")

  
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User created successfully"}

@router.post("/login")
async def client_login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()

    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/files")
async def list_files(db: Session = Depends(get_db)):
    try:
        files = await aws.getAllFiles()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return files


@router.get("/download-file/{filename}")
async def download_file(filename: str, db: Session = Depends(get_db)):
    try:
        link = await aws.downloadFile(filename)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return {"download-link": f"{link}", "message": "sucess"}