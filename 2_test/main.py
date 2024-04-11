from fastapi import FastAPI

from views import router as api_router

app = FastAPI(title="Test App")
app.include_router(api_router)
