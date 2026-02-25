from crewai import Crew
from app.crew.agents import market_agent, news_agent, advisor_agent, manager_agent
from app.crew.crew_factory import create_crew
from app.crew.tasks import market_task, news_task, advisor_task, portfolio_manager_task

def run_crew(coin="bitcoin"):
    crew = create_crew(mode="single")
    result = crew.kickoff(inputs={"coin": coin})
    return result

def run_portfolio_crew(coins: list[str]):
    crew = create_crew(mode="portfolio")
    # Crew će automatski iterirati kroz svaki coin
    result = crew.kickoff(inputs={"portfolio": ", ".join(coins)})
    return result