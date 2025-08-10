from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

template = """
You are an understanding friend who is there to support the person in front of you and relate with them.

Do not offer solutions, just listen to them, validate their emotions, and allow them to vent their frustration. 
Conversation so far:
{chat_history}

User: {user_input}
AI:
"""

prompt = ChatPromptTemplate.from_template(template)
model = OllamaLLM(model="llama3.2", temperature=0.7)
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
chain = LLMChain(
    llm=model,
    prompt=prompt,
    memory=memory,
    verbose=False
)


def respond(user_input):
    result = chain.invoke({"user_input": user_input})

    if isinstance(result, dict):
        return result.get("text") or result.get("content") or str(result)
    
    return str(result)