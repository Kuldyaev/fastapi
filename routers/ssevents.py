from fastapi import APIRouter, Request
import asyncio
from fastapi.responses import StreamingResponse
from sse_starlette.sse import EventSourceResponse
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

STREAM_DELAY = 1  # second
RETRY_TIMEOUT = 15000  # milisecond

@ssevents_router.get('/stream')
async def message_stream(request: Request):
    def new_messages():
        # Add logic here to check for new messages
        yield 'Hello World'
    async def event_generator():
        while True:
            # If client closes connection, stop sending events
            if await request.is_disconnected():
                break

            # Checks for new messages and return them to client if any
            if new_messages():
                yield {
                        "event": "new_message",
                        "id": "message_id",
                        "retry": RETRY_TIMEOUT,
                        "data": "message_content"
                }

            await asyncio.sleep(STREAM_DELAY)

    return EventSourceResponse(event_generator())