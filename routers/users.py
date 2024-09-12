from fastapi import APIRouter, HTTPException, status
from ..models.users import User, UserSignIn

router = APIRouter(
    prefix="/users",
    tags=["Users"] 
)

users = {}

@router.post("/signup")
async def sign_new_user(user: User):
    if user.email in users:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with supplied username exists"
        )
    users[user.email] = user
    return {
        "message": "User successfully registered"
    }
    
@router.post("/signin")
async def sign_in_user(user: UserSignIn):
    if user.email not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="User does not exist"
        )
    print(users[user.email].password)
    if users[user.email].password != user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Wrong credentials passed",
        )
    return {
        "message": "User signed in successfully"
    }
    
    