import chromadb

# 1. Create a persistent ChromaDB client
chroma_client = chromadb.PersistentClient(path="./my_vector_db")

# 2. Created a brand new collection to clear old data
collection = chroma_client.get_or_create_collection(name="english_books")

# 3. Add data to the collection
collection.add(
    documents=[
        "The future of artificial intelligence and robotics",
        "Machine learning and Python programming guide",
        "How to cook delicious biryani and kacchi"
    ],
    metadatas=[
        {"category": "technology", "author": "Munna"},
        {"category": "technology", "author": "Zakir"},
        {"category": "cooking", "author": "Chef Rahman"}
    ],
    ids=["id1", "id2", "id3"]
)

print("✅ Data successfully added to the vector database!\n")

# 4. Define semantic search query
search_query = "computer science"
print(f"🔍 Searching for: '{search_query}'...\n")

results = collection.query(
    query_texts=[search_query],
    n_results=2 
)

# 5. Display search results using proper nested index extraction
print("📋 Search Results:")
for i in range(len(results['documents'][0])):
    document = results['documents'][0][i]
    meta = results['metadatas'][0][i]
    distance = results['distances'][0][i] 
    
    print(f"\n🎯 Result {i+1}:")
    print(f"📖 Book Description: {document}")
    print(f"👤 Author: {meta['author']} | Category: {meta['category']}")
    print(f"📐 Vector Distance: {distance:.4f}")
ls