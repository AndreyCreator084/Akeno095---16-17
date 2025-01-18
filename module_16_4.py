from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel
from typing import List
from typing import Annotated

app = FastAPI()

users = []

class User(BaseModel):
    id: int
    username: str
    age: int

@app.get('/users')
async def get_users()-> List[User]:
    return users

@app.post('/user/{username}/{age}')
async def post_user(
        username: Annotated[str, Path(min_length = 5,
                                      max_length = 20,
                                      description = "Enter username",
                                      example = "UrbanUser")],

        age: Annotated[int, Path(ge = 18,
                                 le = 120,
                                 description= "Enter age",
                                 example = 24)],)-> User:

    new_user_id = max(user.id for user in users) + 1 if users else 1
    new_user = User(id=new_user_id, username=username, age=age)
    users.append(new_user)
    return new_user

@app.put('/user/{user_id}/{username}/{age}')
def update_user(
        user_id: Annotated[int, Path(ge=1,
                                     le=100,
                                     description="Enter User ID",
                                     example=1)],

        username: Annotated[str, Path(min_length = 5,
                                      max_length = 20,
                                      description = "Enter username",
                                      example = "UrbanUser")],

        age: Annotated[int, Path(ge = 18,
                                 le = 120,
                                 description= "Enter age",
                                 example = 24)],)-> User:
    try:
        for user in users:
            if user.id == user_id:
                user.username = username
                user.age = age
                return user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def delete_user(
        user_id: Annotated[int, Path(description="Enter User ID", example=1)],
) -> User:
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User was not found")