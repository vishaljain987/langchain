from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline(
  model_id="",
  task="",
  pipeline_kwargs=dict(
    temperature=0.5,
    max_new_tokens=10
    )
)
      
model = ChatHuggingFace(llm=llm)
result = model.invoke("What is the capital of Belgium")

print(result.content)