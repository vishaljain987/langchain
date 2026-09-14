from langchain_huggingface import HuggingFaceEmbeddings

# HuggingFaceEmbeddings will download the model (~80MB) and needs sentence-transformers package to be able to do that
# skipping this because it will download model in codespaces and my codespaces is running on minimum hardware spec
embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
text = 'What is the capital of Belgium'
documents = [
  "What is the capital of Belgium",
  "What is the capital of Germany"
]
vector = embedding.embed_query(text)
vectors = embedding.embed_documents(documents)


print(str(vector))
print(str(vectors))