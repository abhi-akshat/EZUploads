from sqlalchemy.orm import Session
from db.database import get_db 
from db.models import User
from utils import hash_password

def create_admin_user(db: Session = get_db()):
    admin_username = "admin"
    admin_password = "admin"
    hashed_password = hash_password(admin_password)

    existing_user = db.query(User).filter(User.username == admin_username).first()
    if not existing_user:
        admin_id = "admin"
        admin_user = User(id=admin_id, username=admin_username, password=hashed_password, user_type="admin")
        db.add(admin_user)
        db.commit()
        print("Admin user created.")
    else:
        print("Admin user already exists.")
