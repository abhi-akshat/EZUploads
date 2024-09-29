# EZUploads API

## Overview

The File Management API is a FastAPI application that allows users to manage files through a secure client-server architecture. It supports user authentication, file uploads, downloads, and listing of uploaded files. The application leverages JSON Web Tokens (JWT) for secure access control.

## Features

- User registration (sign-up)
- User login with token-based authentication
- Upload files to the server
- List uploaded files
- Download files from the server
- Secure file management

## Technologies Used

- FastAPI -> Python Framework
- SQLAlchemy -> ORM
- PostgreSQL -> For Database
- JWT (JSON Web Tokens)
- Pydantic -> Data validation
- AWS S3 -> Object Storage to stores files.

## API Endpoints

/admin/login -> Login of Admin User

/admin/files -> List of uploaded files

/admin/upload -> Upload File

/admin/delete-file/{id} -> Deletefile

/login -> Client Login

/signup -> Client Signup

/files -> List of all uploaded file

/download-file/{id} -> Download a particular file.

## File Structure

/EZUploads
├── api
│ ├── **init**.py
│ ├── main.py
│ ├── auth.py
│ ├── aws.py
│ ├── config.py
│ ├── init_db.py
│ ├── utils.py
│ ├── routers
│ │ ├── **init**.py
│ │ ├── admin.py
│ │ ├── client.py
│ └── db
│ ├── **init**.py
│ ├── database.py
│ ├── models.py
├── tests
│ ├── **init**.py
│ ├── test_auth.py
│ ├── test_files.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
