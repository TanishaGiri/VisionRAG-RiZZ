from fastapi import APIRouter, File, UploadFile
import tempfile
from pathlib import Path

from app.services.search_service import SearchService


router = APIRouter(prefix="/search", tags=["search"])


@router.post("/visual")
async def visual_search(file: UploadFile = File(...)):
    suffix = Path(file.filename or "").suffix or ".png"

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp:
        temp.write(await file.read())
        temp_path = temp.name

    try:
        results = SearchService().visual_search(temp_path, top_k=5)

        return [
            {
                "id": result["product"].id,
                "name": result["product"].name,
                "description": result["product"].description,
                "category": result["product"].category,
                "brand": result["product"].brand,
                "price": result["product"].price,
                "currency": result["product"].currency,
                "image_url": result["product"].image_url,
                "distance": result["distance"],
            }
            for result in results
        ]

    finally:
        Path(temp_path).unlink(missing_ok=True)