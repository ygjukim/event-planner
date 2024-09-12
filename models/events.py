from pydantic import BaseModel
from typing import List

class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: List[str]
    location: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will be discussing the contents of the FastAPI book in this ewvent, Ensure to come with you own copy to win gifts!", 
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Goggle Meet",                
            }
        }