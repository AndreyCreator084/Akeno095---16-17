from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root() -> str:
    return "Главная страница"

@app.get("/user/admin")
async def admin() -> str:
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def int_user(user_id: int) -> str:
    return f"Вы вошли как пользователь № {user_id}"

@app.get("/user")
async def info_user(username: str, age: int) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}."