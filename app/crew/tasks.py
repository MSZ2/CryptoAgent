from crewai import Task

def market_task(agent):
    return Task(
        description="""
        Go to this page:
        https://www.coingecko.com/en/coins/{coin}

        Use the scraping tool to extract:
        - Current price
        - 24h change

        Then determine if the trend is:
        - Bullish
        - Bearish
        - Neutral

        Provide a short explanation.
        """,
        expected_output="How the prices changed in the last 24h, current price and the trend",
        agent=agent
    )

def news_task(agent):
    return Task(
        description="""
        Search the web for:
        "{coin} cryptocurrency news last 24 hours"

        Summarize the 3–5 most important news items.

        Determine overall sentiment:
        Positive / Neutral / Negative

        Provide a short explanation.
        """,
        expected_output="Short Explenations of how the news regarding {coin} has been percieved and how the martket is affected",
        agent=agent
    )

def advisor_task(agent):
    return Task(
        description="""
        Based on the market trend analysis and news sentiment for {coin},
        provide:

        - Final recommendation: Buy / Hold / Sell
        - Confidence level (Low/Medium/High)
        - Risk explanation (2–3 sentences)

        Be conservative and realistic.
        """,
        expected_output="""
        - Final recommendation: Buy / Hold / Sell
        - Confidence level (Low/Medium/High)
        - Risk explanation (2–3 sentences)
 """,
        agent=agent
        
    )