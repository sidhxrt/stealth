from fastapi import APIRouter

router = APIRouter()

@router.post("/audio/transcribe")
async def audio_transcriber():
    pass