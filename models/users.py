from pydantic import BaseModel, EmailStr
from typing import Optional, List
from .events import Event

class User(BaseModel):
    email: EmailStr
    password: str
    username: str
    events: Optional[list[Event]]

    class Config:
        json_shema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!",
                "username": "fastapi",
            }
        }
        
class UserSignIn(BaseModel):
    email: EmailStr
    password: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!",
            }
        }        