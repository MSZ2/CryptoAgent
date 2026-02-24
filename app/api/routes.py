from fastapi import APIRouter
from pydantic import BaseModel
from app.crew.crew_setup import run_crew

router = APIRouter()

class Query(BaseModel):
    coin: str = "bitcoin"

@router.post("/advise")
def advise(q: Query):
    result = run_crew(q.coin)
    print(type(result))
    return {"advice": result.raw}