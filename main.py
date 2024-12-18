from fastapi import FastAPI, Path
import uvicorn

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/")
async def read_root():
    return {"Главная страница"}


@app.get("/users")
async def read_user_all()-> dict:
    return users

@app.post('/user/{username}/{age}')
async def create_user(username, age):
    print(len(users))
    new_id = str(len(users) + 1)
    new_data = f'Имя: {username}, возраст: {age}'
    users[new_id]=new_data
    return {f'User {new_id} is registered'}

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id,username, age):
    new_data = f'Имя: {username}, возраст: {age}'
    users[user_id]=new_data
    return {f'The user {user_id} is updated'}

@app.delete('/user/{user_id}')
async def delete_user(user_id):
    del users[user_id]
    return {f'User {user_id} has been deleted'}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8005)
