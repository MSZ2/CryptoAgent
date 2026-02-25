from fastapi import APIRouter
from pydantic import BaseModel
from app.crew.crew_runner import run_crew, run_portfolio_crew

router = APIRouter()


class CoinQuery(BaseModel):
    coin: str


class PortfolioQuery(BaseModel):
    coins: list[str]


@router.post("/advise")
def advise(q: CoinQuery):
    result = run_crew(q.coin)
    return {"result": result.raw}


@router.post("/portfolio/advice")
def portfolio_advice(q: PortfolioQuery):
    result = run_portfolio_crew(q.coins)
    return {"result": result.raw}