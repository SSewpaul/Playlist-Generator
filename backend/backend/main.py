from fastapi import FastAPI
from endpoints.routers import endpoint_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title='playlist generator', docs_url='/docs')

origins = [
    'http://localhost:5173'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(endpoint_router)


