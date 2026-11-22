from pydantic import BaseModel, Field

class Product(BaseModel):
    id: str
    name: str
    description: str
    category: str
    brand: str | None = None
    price: float = Field(gt=0)
    currency: str = "INR"
    image_url: str | None = None
    tags: list[str] = []
