from fastapi import FastAPI
from app.database import engine, Base
from app.routes import router

Base.metadata.create_all(bind=engine)
app = FastAPI(
    title= "URL Shortener",
    description="API para encurtar URLs com estatísticas de acesso.",
    version="1.0",
)

app.include_router(router)