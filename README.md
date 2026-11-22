
# VisionRAG-Rizz 🛍️🤖

### Multimodal AI-Powered Product Discovery & Intelligent Shopping Assistant

VisionRAG Commerce is an AI-powered product discovery platform that combines **Computer Vision, Natural Language Processing, Retrieval-Augmented Generation (RAG), and Hybrid Search** to make online shopping more intelligent.

Instead of relying only on traditional keyword-based search, users can discover products using natural language queries and visual similarity. The platform uses CLIP-based image embeddings, vector search, BM25 keyword retrieval, and LLM-powered responses to deliver context-aware product recommendations.

## ✨ Key Features

- **Multimodal Product Search:** Search for products using text descriptions and images.
- **CLIP Image Embeddings:** Understand visual similarities between product images using CLIP.
- **Semantic Search:** Retrieve relevant products based on the meaning and context of user queries.
- **Vector Database:** Store and retrieve product embeddings using ChromaDB.
- **Hybrid Retrieval:** Combine semantic vector search with BM25 keyword-based retrieval.
- **RAG Pipeline:** Generate context-aware responses using retrieved product information.
- **AI Shopping Assistant:** Provide intelligent product discovery and recommendations.
- **Full-Stack Integration:** React-based frontend connected to a FastAPI backend.

## 🧠 How It Works

1. **Product Ingestion:** Product information and images are loaded into the system.
2. **Embedding Generation:** CLIP generates image embeddings, while text embedding models generate semantic representations.
3. **Vector Indexing:** Embeddings are stored in ChromaDB for efficient similarity search.
4. **Query Processing:** Users submit natural-language queries or product images.
5. **Hybrid Retrieval:** Semantic similarity search and BM25 retrieval identify relevant products.
6. **Context Generation:** Retrieved product information is passed into the LLM context.
7. **Response Generation:** The LLM generates context-aware responses based on retrieved products.

## 🏗️ Architecture

```text
                 USER
                   |
                   v
          React / Next.js UI
                   |
                   v
              FastAPI
                   |
          +--------+--------+
          |                 |
          v                 v
    Text Processing    Image Processing
          |                 |
          v                 v
   Text Embeddings     CLIP Embeddings
          |                 |
          +--------+--------+
                   |
                   v
             Hybrid Search
                   |
          +--------+--------+
          |                 |
          v                 v
       ChromaDB           BM25
          |                 |
          +--------+--------+
                   |
                   v
            Retrieved Context
                   |
                   v
             LLM Integration
                   |
                   v
       Context-Aware Response
```

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Frontend | React, Next.js |
| Backend | Python, FastAPI |
| Computer Vision | CLIP |
| Embeddings | CLIP, Sentence Transformers |
| Vector Database | ChromaDB |
| Retrieval | Semantic Search, BM25 |
| Generative AI | Large Language Models (LLMs) |
| API Integration | REST APIs |
| Package Management | uv |

## 🚀 Getting Started

### Prerequisites

- Python 3.12+
- Node.js
- uv package manager
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/TanishaGiri/VisionRAG-RiZZ.git

cd VisionRAG-RiZZ
```

### 2. Backend Setup

```bash
cd backend

uv sync
```

Create a `.env` file in the backend directory and configure the required environment variables:

```env
LLM_API_KEY=your_api_key_here
```

Start the FastAPI server:

```bash
uv run uvicorn app.main:app --reload
```

Backend API:

```text
http://localhost:8000
```

API Documentation:

```text
http://localhost:8000/docs
```

### 3. Frontend Setup

Open another terminal:

```bash
cd frontend

npm install

npm run dev
```

Open the application:

```text
http://localhost:3000
```

## 🔍 Example Use Cases

- Find a black dress with a minimalist design.
- Discover products visually similar to an uploaded image.
- Search for products using descriptive natural-language queries.
- Retrieve relevant products using semantic and keyword-based search.
- Get AI-assisted product discovery based on retrieved catalog information.

## 🎯 Project Objective

The objective of VisionRAG Commerce is to explore how multimodal AI and Retrieval-Augmented Generation can improve traditional e-commerce search experiences.

By combining visual understanding, semantic retrieval, hybrid search, and LLM-based response generation, the project demonstrates an intelligent approach to product discovery.

## 👩‍💻 Author

**Tanisha Giri**

Software Engineer | AI/ML & Generative AI Enthusiast

- GitHub: [@TanishaGiri](https://github.com/TanishaGiri)

---

⭐ If you find this project interesting, consider giving the repository a star!
