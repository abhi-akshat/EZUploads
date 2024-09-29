import os
import bcrypt
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from config import settings

def hash_password(password: str) -> str:
    """Hash a password using bcrypt."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plain password against a hashed password."""
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
    """Create a JWT token."""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def get_file_download_link(filename: str) -> str:
    """Generate a secure download link for a file."""
    # Ensure the uploads directory exists
    uploads_path = os.path.join(os.getcwd(), "uploads")  # Get current working directory
    file_path = os.path.join(uploads_path, filename)

    if os.path.exists(file_path):
        # Assuming you have a route set up in your FastAPI to serve files
        return f"https://yourdomain.com/api/download/{filename}"  # Adjust to your actual domain and route
    else:
        raise FileNotFoundError(f"The file {filename} does not exist.")