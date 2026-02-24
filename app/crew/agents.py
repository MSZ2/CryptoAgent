from crewai import Agent
from app.core.llm import gemini_llm
from crewai_tools import ScrapeWebsiteTool, SerperDevTool

scrape_tool = ScrapeWebsiteTool(website_url="https://www.coingecko.com/")
search_tool = SerperDevTool()

market_agent = Agent(
    role="Crypto Market Analyst",
    backstory="I analyze market trends and provide insights on price movements and trading opportunities.",
    goal="Analyze crypto price trends  in real-time",
    tools=[scrape_tool],
    llm=gemini_llm,
    verbose=True
)

news_agent = Agent(
    role="Crypto News Analyst",
    backstory="I keep track of the latest news in the crypto world and provide summaries and insights.",
    goal="Find and summarize latest crypto news and give insights how could it affect the market",
    tools=[search_tool],
    llm=gemini_llm,
    verbose=True
)

advisor_agent = Agent(
    role="Trading Advisor",
    backstory="I provide personalized trading advice based on market analysis and news insights.",
    goal="Provide Buy/Hold/Sell recommendation",
    llm=gemini_llm,
    verbose=True
)