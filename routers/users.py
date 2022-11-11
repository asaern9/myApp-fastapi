from fastapi import APIRouter, Path, HTTPException
from urllib.parse import quote
import requests
from schemas.users import Users

router = APIRouter()


@router.get('/users')
async def read_users():
    """This endpoint is used to read all user data from the json placeholder website """
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    result = response.json()
    if result:
        return result
    else:
        raise HTTPException


@router.get('/user/{user_id}')
async def read_single_user(user_id: int = Path(ge=1, lt=10)):
    """This endpoint is used to read a specific user data from the json placeholder website """
    path_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(quote(str(user_id)))
    response = requests.get(path_url)
    result = response.json()
    if result:
        return result
    else:
        raise HTTPException


@router.post('/users')
async def write_user(user: Users):
    """ This endpoint is used to save a user data to the json placeholder website """
    path_url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.post(path_url, user.json())
    if response:
        return user
    else:
        raise HTTPException


@router.put('/users')
async def update_user(user: Users, user_id: int):
    """ This endpoint is used to update a specific user data to the json placeholder website """
    path_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(quote(str(user_id)))
    response = requests.put(path_url, user.json())
    if response:
        return user
    else:
        raise HTTPException


@router.delete('/users')
async def delete_user(user_id: int):
    """ This endpoint is used to delete a user data to the json placeholder website """
    path_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(quote(str(user_id)))
    response = requests.delete(path_url)
    if response:
        return response
    else:
        raise HTTPException