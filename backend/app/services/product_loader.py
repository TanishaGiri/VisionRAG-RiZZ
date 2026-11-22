import json
from pathlib import Path

from app.models.product import Product

DATA_FILE = Path(__file__).resolve().parents[3]/"data"/"products.json"

def load_products() -> list[Product]:
    with DATA_FILE.open("r", encoding="utf-8") as file:
        data = json.load(file)

        return [Product(**item) for item in data]
    
def get_product_by_id(product_id: str) -> Product | None:
    products = load_products()

    for product in products:
        if product.id == product_id:
            return product

    return None