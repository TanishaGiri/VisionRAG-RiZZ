from app.services.embedding_service import EmbeddingService
from app.services.product_loader import load_products
from app.services.vector_store import VectorStore

class IndexingService:
    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.vector_store = VectorStore()

    def index_products(self):
        products = load_products()

        documents = [
            (
                f"{product.name}. "
                f"{product.description}. "
                f"Category: {product.category}. "
                f"Brand: {product.brand or ''}."
                f"Tags: {', '.join(product.tags)}."
            )
            for product in products
        ]

        embeddings = self.embedding_service.embed_texts(documents)

        self.vector_store.add_products(
            ids=[product.id for product in products],
            documents=documents,
            embeddings=embeddings,
        )

        return len(products)