from crewai import Crew
from app.crew.agents import market_agent, news_agent, advisor_agent
from app.crew.tasks import market_task, news_task, advisor_task

def run_crew(coin="bitcoin"):
    tasks = [
        market_task(market_agent),
        news_task(news_agent),
        advisor_task(advisor_agent)
    ]

    crew = Crew(
        agents=[market_agent, news_agent, advisor_agent],
        tasks=tasks,
        verbose=True
    )

    result = crew.kickoff(inputs={"coin": coin})
    return result