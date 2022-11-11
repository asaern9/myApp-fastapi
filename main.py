from fastapi import FastAPI
from routers import users
from routers import posts

app = FastAPI(title="Testing JsonPlaceHolder Api")

app.include_router(posts.router, tags=['POSTS'])
app.include_router(users.router, tags=['USERS'])


@app.get('/')
async def root():
    """ This is the root endpoint """
    return "Hey"


'''
@app.get('/posts/{post_id}')
async def get_post_route(post_id: int = Path(title='ID of the particular post to get', ge=1)):
    post = posts[(post_id-1)]
    return post


@app.post('/posts')
async def save_post_route(post: Post):
    posts.append(post)
    print(post)
    return "Post added successfully"


@app.put('/posts/{post_id}')
async def update_post_route(post: Post, post_id: int = Path(title='ID of the post to be updated', ge=1)):
    update_post = jsonable_encoder(post)
    posts[post_id-1] = update_post
    print(posts[post_id-1])
    return "Post updated successfully"


@app.patch('/posts/{post_id}')
async def update_post_route(post: PostUpdate, post_id: int = Path(title='ID of the post to be updated', ge=1)):
    old_post_data = posts[post_id]
    old_post_model = PostUpdate(**old_post_data)
    update_post_data = post.dict(exclude_unset=True)
    update_post = old_post_model.copy(update=update_post_data)
    posts[post_id-1] = jsonable_encoder(update_post)
    print(posts[post_id-1])
    return "Post updated successfully"


@app.delete('/posts/{post_id}')
async def delete_post(post_id: int = Path(title='ID of the post to be updated', ge=1)):
    data_to_delete = posts.pop(post_id-1)
    print(data_to_delete)
    return "Post deleted successfully"

'''

