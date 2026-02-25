# Crypto Trading Advisor (CrewAI + FastAPI)

AI-powered crypto analysis service that provides **Buy / Hold / Sell**
recommendations using a multi-agent architecture built with CrewAI.

## Features

-   Multi-agent system using CrewAI
    -   Market Analyst (price trends)
    -   News Analyst (web search sentiment)
    -   Trading Advisor (final decision)
    -   Portfolio Manager (delegates and aggregates)
-   Single coin analysis
-   Portfolio analysis
-   CoinGecko scraping
-   Real-time news via Serper
-   Gemini-based LLM
-   FastAPI backend
-   Simple frontend
-   Docker support

------------------------------------------------------------------------

## Run with Docker

Build image:

    sudo docker build -t cryptoadvisor .

Run container:

    docker run -p 8000:8000 \
        -e SERPER_API_KEY="your_serper_api_key" \
        -e GOOGLE_API_KEY="your_google_api_key" \
        -e GROQ_API_KEY="your_groq_api_key" \
        cryptoadvisor

Open:

    http://localhost:8000/

------------------------------------------------------------------------

## API Endpoints

### Single Coin

POST /advise

Request: { "coin": "bitcoin" }

------------------------------------------------------------------------

### Portfolio

POST /portfolio/advice

Request: { "coins": \["bitcoin", "ethereum", "solana"\] }

Returns: - Per-coin recommendations - Portfolio risk - Allocation
suggestions - Overall strategy

------------------------------------------------------------------------

## Tech Stack

-   Python 3.12
-   FastAPI
-   CrewAI
-   Google Gemini
-   Serper API
-   Docker
-   HTML + JavaScript

------------------------------------------------------------------------

## Disclaimer

This project is for educational purposes only. Not financial advice.
