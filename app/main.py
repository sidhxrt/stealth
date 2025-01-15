from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def starter_func():
    return "stealth"