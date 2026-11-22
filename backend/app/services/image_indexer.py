import io
import requests
from PIL import Image

from app.models.product import Product
from app.services.image_embedder import ImageEmbedder
from app.services.vector_store import VectorStore


class ImageIndexer:
    def __init__(self):
        self.embedder = ImageEmbedder()
        self.vector_store = VectorStore()

    def index_product(self, product: Product):
        if not product.image_url:
            return

        url = product.image_url

        if "placehold.co" in url and "/png" not in url:
            url = url.replace("placehold.co/600x800", "placehold.co/600x800/png")

        response = requests.get(url, timeout=30)
        response.raise_for_status()

        image = Image.open(io.BytesIO(response.content)).convert("RGB")

        inputs = self.embedder.processor(
            images=image,
            return_tensors="pt"
        )

        output = self.embedder.model.get_image_features(**inputs)

        embedding = (
            output.pooler_output
            if hasattr(output, "pooler_output")
            else output
        )

        embedding = embedding[0].detach().cpu().tolist()

        self.vector_store.add_image_products(
            ids=[product.id],
            embeddings=[embedding],
        )