from fastapi import FastAPI
from .routers import users, events

app = FastAPI()

app.include_router(users.router)
app.include_router(events.router)

@app.get("/")
async def home():
    return {
        "Welcome to Event Planner APP."
    }