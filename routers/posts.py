from fastapi import APIRouter, Path, HTTPException, status, Body
from urllib.parse import quote
import requests
from schemas.posts import Post

router = APIRouter()


@router.get('/posts', status_code=status.HTTP_200_OK)
async def read_post():
    """ This endpoint is used to read all the posts data from json placeholder website"""
    result = requests.get('https://jsonplaceholder.typicode.com/posts')
    response = result.json()[:50]
    if response:
        return response
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.get('/posts/{post_id}', status_code=status.HTTP_200_OK)
async def read_single_post(post_id: int = Path(ge=1)):
    """ This endpoint is used to read a specific post data from the json placeholder website """
    path_url = 'https://jsonplaceholder.typicode.com/posts/{}'.format(quote(str(post_id)))
    result = requests.get(path_url)
    response = result.json()
    if response:
        return response
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.post('/posts/', status_code=status.HTTP_201_CREATED)
async def write_post(post: Post):
    """ This endpoint is used to save a post data to the json placeholder website """
    path_url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.post(path_url, post.json())
    if response:
        return post
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.put('/posts', status_code=status.HTTP_201_CREATED)
async def update_post(post: Post, post_id: int):
    """ This endpoint is used to update a specific post data to the json placeholder website """
    path_url = 'https://jsonplaceholder.typicode.com/posts/{}'.format(quote(str(post_id)))
    result = requests.put(path_url, post.json())
    if result.status_code == 200:
        return post
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.delete('/posts', status_code=status.HTTP_200_OK)
async def delete_post(post_id: int=Body(title="ID of the post to be deleted")):
    """ This endpoint is used to delete a specific post data to the json placeholder website """
    path_url = 'https://jsonplaceholder.typicode.com/posts/{}'.format(quote(str(post_id)))
    response = requests.delete(path_url)
    if response:
        return response
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)



#hery fjsdfkasdfasdf