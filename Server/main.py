#fastapi entry point

from fastapi import FastAPI
from auth_routes import router as auth_router

app = FastAPI(title="Virtual ID Authentication API")

# Include authentication routes
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Virtual ID Authentication API"}
