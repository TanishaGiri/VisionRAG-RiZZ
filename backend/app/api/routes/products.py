from fastapi import APIRouter, Query

from app.models.product import Product
from app.services.product_loader import load_products
from app.services.search_service import SearchService

router = APIRouter(prefix="/products", tags=["Products"])

search_service = SearchService()


@router.get("/", response_model=list[Product])
def get_products():
    return load_products()


@router.get("/search", response_model=list[Product])
def search_products(
    q: str = Query(..., min_length=1),
    top_k: int = Query(5, ge=1, le=20),
):
    results = search_service.semantic_search(q, top_k)

    ids = results.get("ids", [[]])[0]

    all_products = load_products()

    return [
        product
        for product in all_products
        if product.id in ids
    ]

@router.get("/search/hybrid", response_model=list[Product])
def hybrid_search_products(
    q: str = Query(..., min_length=1),
    top_k: int = Query(5, ge=1, le=20),
):
    results = search_service.hybrid_search(q, top_k)

    return [
        result["product"]
        for result in results
    ]
# @router.get("/search")
# def search_products(
#     q: str = Query(..., min_length=1),
#     top_k: int = Query(5, ge=1, le=20),
# ):
#     return search_service.semantic_search(q, top_k)