from fastapi import APIRouter

from backend.endpoints import filter

endpoint_router = APIRouter()
endpoint_router.include_router(filter.router, prefix='/filter', tags=['filter'])