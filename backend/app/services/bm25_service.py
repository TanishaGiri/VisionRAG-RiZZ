from rank_bm25 import BM25Okapi

from app.services.product_loader import load_products


class BM25Service:
    def __init__(self):
        self.products = load_products()

        self.documents = [
            f"{product.name} {product.description} "
            f"{product.category} {product.brand}"
            for product in self.products
        ]

        tokenized_documents = [
            document.lower().split()
            for document in self.documents
        ]

        self.bm25 = BM25Okapi(tokenized_documents)

    def search(self, query: str, top_k: int = 5):
        tokenized_query = query.lower().split()

        scores = self.bm25.get_scores(tokenized_query)

        ranked_indices = sorted(
            range(len(scores)),
            key=lambda index: scores[index],
            reverse=True,
        )[:top_k]

        return [
            {
                "product": self.products[index],
                "score": scores[index],
            }
            for index in ranked_indices
            if scores[index] > 0
        ]