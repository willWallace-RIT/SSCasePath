from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="CasePath API")

app.include_router(router)

@app.get("/")
def root():
    return {"status": "CasePath API running"}
