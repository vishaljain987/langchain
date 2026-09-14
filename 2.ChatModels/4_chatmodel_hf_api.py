from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

llm=HuggingFaceEndpoint(repo_id="meta-llama/Llama-3.1-8B-Instruct",
                        task="text-generation")
model = ChatHuggingFace(llm=llm)
result = model.invoke("What is the capital of Belgium")

print(result.content)