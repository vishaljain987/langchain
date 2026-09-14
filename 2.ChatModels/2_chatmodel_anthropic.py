from langchain_anthropic import ChatAnthropic

model = ChatAnthropic(model='claude-3-5-sonnet-20241022')
result=model.invoke("what is the capital of Belgium")

print(result.content)