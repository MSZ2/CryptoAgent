from crewai import Crew, Process

from app.crew.agents import (
    market_agent,
    news_agent,
    advisor_agent,
    manager_agent
)

from app.crew.tasks import (
    market_task,
    news_task,
    advisor_task,
    portfolio_manager_task
)


def create_crew(mode: str = "single"):
    """
    mode:
        'single'    -> classic sequential crew (per coin)
        'portfolio' -> hierarchical crew with manager
    """

    # Base agents used in both modes
    base_agents = [market_agent, news_agent, advisor_agent]

    # Base tasks (per coin analysis)
    base_tasks = [
        market_task(market_agent),
        news_task(news_agent),
        advisor_task(advisor_agent)
    ]

    if mode == "single":
        # Your current behavior
        return Crew(
            agents=base_agents,
            tasks=base_tasks,
            process=Process.sequential,
            verbose=True
        )

    elif mode == "portfolio":
        # Add manager task
        tasks =[
            portfolio_manager_task(manager_agent)
        ]

        return Crew(
            agents=base_agents,
            tasks=tasks,
            manager_agent=manager_agent,
            process=Process.hierarchical,
            verbose=True
        )

    else:
        raise ValueError("Invalid crew mode")