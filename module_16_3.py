# uvicorn module16.module_16_3:app --reload

from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/user')
async def get_message() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def post_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username')],
                    age: Annotated[int, Path(ge=18, le=120, description='Enter age')]) -> str:
    new_user_id = str(max(map(int, users.keys()), default=0) + 1)
    users[new_user_id] = f'Имя: {username}, возраст: {age}'
    return f"User {new_user_id} is registered"


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID')],
                      username: str, age: str):
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f"The user {user_id} is registered"


@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[str, Path(min_length=1, max_length=100, description='Enter User ID')]):

    users.pop(user_id)
    return f"User {user_id} has been deleted"

