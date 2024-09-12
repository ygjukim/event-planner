from fastapi import APIRouter, Body, HTTPException, status
from ..models.events import Event
from typing import List

router = APIRouter(
    prefix="/events",
    tags = [ "Events"],
)

events = []

@router.get("/", response_model=List[Event])
async def retrieve_all_events():
     return events
 
@router.get("/{id}", response_model=Event)
async def retrieve_event(id: int):
    for event in events:
         if event.id == id:
             return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID dess not exist",
    )
    
@router.post("/new")
async def create_event(body: Event = Body(...)):
    events.append(body)
    return {
        "message": "Event created succcessfully"    
    }
    
@router.put("/update")
async def update_event(body: Event = Body(...)):
    for event in events:
        if event.id == body.id:
            updated_event = event.model_copy(
                update=body.model_dump(),
                deep=True,
            )
            events.remove(event)
            events.append(updated_event)
            return updated_event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID dess not exist",
    )

@router.delete("/{id}")
async def delete_event(id: int):
    for event in events:
        if event.id == id:
            events.remove(event)
            return {
                "message": "Event deleted succcessfully"
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID dess not exist",
    )

@router.delete("/")
async def delete_all_events():
    events.clear()
    return {
        "message": "All Events deleted succcessfully"
    }            