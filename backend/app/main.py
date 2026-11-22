from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes.health import router as health_router
from app.api.routes.products import router as products_router
from app.api.routes.visual_search import router as visual_search_router

app = FastAPI(
    title="VisionRAG Commerce API",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(health_router)
app.include_router(products_router)
app.include_router(visual_search_router)

# @app.get("/")
# def root():
#     return {
#         "message": "VisionRAG Commerce API is running",
#         "version": "0.1.0",
#     }


# @app.get("/health")
# def health():
#     return {"status": "healthy"}