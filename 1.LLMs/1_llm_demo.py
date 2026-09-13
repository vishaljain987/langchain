from langchain_openai import OpenAI

# below two lines are not needed as secret comes from env variables from codespaces
# from dotenv import load_dotenv
# load_dotenv()
llm = OpenAI(model='gpt-3.5-turbo-instruct')
result = llm.invoke("What is the capital of Canada")
print(result)