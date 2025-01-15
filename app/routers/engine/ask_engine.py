from fastapi import APIRouter

router = APIRouter()

@router.post("/text/ask")
async def ask_engine_query():
    pass