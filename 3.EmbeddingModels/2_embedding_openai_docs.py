from langchain_openai import OpenAIEmbeddings

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

documents = [
  "What is the capital of Belgium",
  "What is the capital of Germany"
]
result = embedding.embed_documents(documents)

print(str(result))