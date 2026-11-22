from functools import lru_cache
from app.services.embedding_service import EmbeddingService
from app.services.vector_store import VectorStore
from app.services.bm25_service import BM25Service

@lru_cache(maxsize=1)
def get_image_embedder():
    from app.services.image_embedder import ImageEmbedder
    return ImageEmbedder()

class SearchService:
    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.vector_store = VectorStore()
        self.bm25_service = BM25Service()

    def semantic_search(self, query: str, top_k: int = 5):
        query_embedding = self.embedding_service.embed_text(query)
        results = self.vector_store.search(query_embedding, top_k)

        distances = results.get("distances", [[]])[0]
        ids = results.get("ids", [[]])[0]
        documents = results.get("documents", [[]])[0]

        filtered_ids = []
        filtered_documents = []
        filtered_distances = []

        for product_id, document, distance in zip(
            ids, documents, distances
        ):
            if distance <= 0.80:
                filtered_ids.append(product_id)
                filtered_documents.append(document)
                filtered_distances.append(distance)

        results["ids"] = [filtered_ids]
        results["documents"] = [filtered_documents]
        results["distances"] = [filtered_distances]

        return results

    def keyword_search(self, query: str, top_k: int = 5):
        return self.bm25_service.search(query, top_k)

    def hybrid_search(self, query: str, top_k: int = 5):
        semantic_results = self.semantic_search(query, top_k)
        keyword_results = self.keyword_search(query, top_k)

        scores = {}
        products = {}

        for rank, product_id in enumerate(
            semantic_results.get("ids", [[]])[0],
            start=1,
        ):
            scores[product_id] = scores.get(product_id, 0) + 1 / (60 + rank)

        for rank, result in enumerate(keyword_results, start=1):
            product_id = result["product"].id

            scores[product_id] = scores.get(product_id, 0) + 1 / (60 + rank)
            products[product_id] = result["product"]

        for product_id in semantic_results.get("ids", [[]])[0]:
            if product_id not in products:
                from app.services.product_loader import get_product_by_id
                products[product_id] = get_product_by_id(product_id)

        ranked_ids = sorted(
            scores,
            key=scores.get,
            reverse=True,
        )[:top_k]

        return [
            {
                "product": products[product_id],
                "score": scores[product_id],
            }
            for product_id in ranked_ids
            if products.get(product_id)
        ]

    def visual_search(self, image_path: str, top_k: int = 5):
        from app.services.product_loader import get_product_by_id

        image_embedder = get_image_embedder()
        query_embedding = image_embedder.embed_image(image_path)

        results = self.vector_store.search_images(
            query_embedding=query_embedding,
            top_k=top_k,
        )

        product_ids = results.get("ids", [[]])[0]
        distances = results.get("distances", [[]])[0]

        products = []

        for product_id, distance in zip(product_ids, distances):
            product = get_product_by_id(product_id)

            if product and distance <= 0.30:
                products.append({
                    "product": product,
                    "distance": distance,
                })

        return products
    # def semantic_search(self, query: str, top_k: int = 5):
    #     query_embedding = self.embedding_service.embed_text(query)


    #     return self.vector_store.search(
    #         query_embedding=query_embedding,
    #         top_k=top_k,
    #     )