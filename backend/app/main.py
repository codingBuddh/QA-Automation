from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import stock_routes
from app.config import settings
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory=str(settings.STATIC_DIR)), name="static")

# Include routers
app.include_router(stock_routes.router, prefix=f"{settings.API_V1_STR}/stocks", tags=["stocks"]) 