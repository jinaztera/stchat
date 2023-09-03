# from dotenv import load_dotenv
# load_dotenv()
# from langchain.llms import OpenAI
# llm = OpenAI(openai_api_key="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")

# result = llm.predict("기분이 어때?")

# print(result)

from langchain.chat_models import ChatOpenAI
llm = ChatOpenAI(openai_api_key="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")

result = llm.predict("저녁 메뉴 추천해줘")

print(result)