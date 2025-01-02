from fastapi import APIRouter
from fastapi.responses import StreamingResponse
import time

ssevents_router = APIRouter(
   prefix="/ssevents",
   tags=["SSEvents"],
)

def fake_video_streamer():
    for i in range(10):
        yield f"frame {i}\n"
        time.sleep(1)

@ssevents_router.get("/")
async def main():
    return StreamingResponse(fake_video_streamer(), media_type="text/plain")