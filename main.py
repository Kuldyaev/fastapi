from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from a2wsgi import ASGIMiddleware
from routers import router as api_router
import uvicorn

app = FastAPI()

app.add_middleware(
   CORSMiddleware, 
   allow_origins=["*"],
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"], 
)

templates = Jinja2Templates(directory='templates')

app.include_router(api_router)
    
@app.get("/")
async def home_page(request: Request):
   return templates.TemplateResponse(name='home.html', context={'request': request})

application = ASGIMiddleware(app)

if __name__ == "__main__":    
   uvicorn.run(application, host='0.0.0.0', log_level='info')