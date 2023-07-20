from fastapi import APIRouter
from backend.schemas.filters import Filters

router = APIRouter()

@router.post('/')
def filter(
    search_words: str,
    filters: Filters
):
    print(filters)

    return filters