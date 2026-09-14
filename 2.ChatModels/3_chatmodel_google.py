from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')
result=model.invoke("what is the capital of Belgium")

print(result.content)