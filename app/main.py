from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Crypto Trading Advisor")
app.include_router(router)