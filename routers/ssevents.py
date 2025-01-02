from fastapi import APIRouter
from fastapi.responses import StreamingResponse

ssevents_router = APIRouter(
   prefix="/ssevents",
   tags=["SSEvents"],
)

async def fake_video_streamer():
    for i in range(10):
        yield b"some fake video bytes"

@ssevents_router.get("/")
async def main():
    return StreamingResponse(fake_video_streamer())