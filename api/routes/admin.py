from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from utils import verify_password, create_access_token
from db.database import get_db
from db.models import User
import aws
import os

router = APIRouter()

@router.post("/login")
async def admin_login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    if user.user_type != "admin":
        raise HTTPException(status_code=403, detail="Not an admin user")
    
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/upload")
async def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    allowed_types = [
        "application/vnd.openxmlformats-officedocument.presentationml.presentation", 
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",    
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"        
    ]
    
    if file.content_type not in allowed_types:
        raise HTTPException(status_code=400, detail="Invalid file type")
    
    try:
        await aws.upload_file(file.filename, file.file)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return {"info": f"File '{file.filename}' uploaded successfully"}

@router.get("/files")
async def list_files(db: Session = Depends(get_db)):
    try:
        files = await aws.getAllFiles()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return files


@router.delete("/delete-file/{fileid}")
async def delete_file(fileid: str, db: Session = Depends(get_db)):
    try:
        files = await aws.deleteFile(fileid)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return files