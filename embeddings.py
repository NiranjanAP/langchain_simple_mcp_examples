import os
from langchain.chat_models import init_chat_model

os.environ["GOOGLE_API_KEY"] = input("Enter google api key")

model = init_chat_model("google_genai:gemini-2.5-flash-lite")

from langchain_google_genai import GoogleGenerativeAIEmbeddings
embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

texts = [
    "What is the meaning of life?",
    "What is the purpose of existence?",
    "How do I bake a cake?"]


from langchain_chroma import Chroma

# Create vector store from texts
vectorstore = Chroma.from_texts(
    texts=texts,
    embedding=embeddings,
)

for text in texts:
    # Now you can query it
    results = vectorstore.similarity_search_with_score(text, k=3)

    # Method 3: Pretty table format
    print("=" * 60)
    print("Results for:", text)
    print("Score\tContent")
    print("-" * 60)
    for doc, score in results:
        print(f"{score:.4f}\t{doc.page_content[:100]}...")





