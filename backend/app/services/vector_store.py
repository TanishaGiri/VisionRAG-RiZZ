from pathlib import Path

import chromadb

CHROMA_PATH = Path(__file__).resolve().parents[3]/"data"/"chroma"


class VectorStore:
    def __init__(self):
        self.client = chromadb.PersistentClient(path=str(CHROMA_PATH))

        self.collection = self.client.get_or_create_collection(
            name="products",
            metadata={"hnsw:space": "cosine"},
        )

    def add_products(
            self,
            ids: list[str],
            documents: list[str],
            embeddings: list[list[float]],
    ):
        self.collection.upsert(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
        )

    def search(
            self,
            query_embedding: list[float],
            top_k: int = 5,
    ):
        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
        )

    def add_image_products(
            self,
            ids: list[str],
            embeddings: list[list[float]],
    ):
        image_collection = self.client.get_or_create_collection(
            name="product_images",
            metadata={"hnsw:space": "cosine"},
        )

        image_collection.upsert(
            ids=ids,
            embeddings=embeddings,
        )

    def search_images(
            self,
            query_embedding: list[float],
            top_k: int = 5,
    ):
        image_collection = self.client.get_or_create_collection(
            name="product_images",
            metadata={"hnsw:space": "cosine"},
        )

        return image_collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
        )

    def delete_image_products(self, ids: list[str]):
        image_collection = self.client.get_or_create_collection(
            name="product_images",
            metadata={"hnsw:space": "cosine"},
        )

        image_collection.delete(ids=ids)