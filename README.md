# 🤖 Semantic Search Engine using ChromaDB

A lightweight, high-performance vector search engine implementation built on top of Python and ChromaDB. This repository documents a functional architecture designed to handle semantic retrieval workflows, high-dimensional vector embeddings, and contextual similarity queries without requiring external third-party API dependencies.

---

## 📂 Project Architecture

The workspace footprint is engineered to keep processing files clean, decoupled, and isolated:

```text
├── main.py              # Application entry point handling vector insertion and queries
├── .gitignore           # Version tracking filters keeping databases out of source control
└── README.md            # Technical system documentation and deployment guidelines
```

---

## 🛠️ Tech Stack & Core Libraries

* **Core Engine**: Python 3.10+
* **Vector Database**: ChromaDB (Local Persistent Engine)
* **Embedding Model**: Default `all-MiniLM-L6-v2` (Built directly into local system runtime)

---

## 🚀 Getting Started

Follow these operational steps to deploy and execute this vector pipeline locally on your development machine:

### 1. Initialize Project Directory
Navigate into your system workspace folder using your terminal interface:
```bash
cd C:\Users\TNS-07\RAG
```

### 2. Install Engine Dependencies
Install the required vector database modules using the Python package index wrapper:
```bash
pip install chromadb
```

### 3. Run Semantic Queries
Execute the core Python runtime script to construct your database, embed unstructured entries, and run vector distance searches:
```bash
python main.py
```

---

## 🔬 System Behavior & Verification

When initialized, the system automatically bypasses literal token-matching to track structural context maps:
1. **Ingestion Loop**: Data fields are mapped to a collection (`english_books`) with specific categorical markers.
2. **Persistence Layer**: Data frames serialize locally under a persistent folder layout (`./my_vector_db`).
3. **Distance Search**: Query parameters (e.g., searching for `"computer science"`) evaluate mathematical proximity vectors to retrieve contextual records (like Machine Learning documents) while passing over unrelated nodes.

---

## 📄 License
Distributed under the MIT License. See local tracking guidelines for details.
