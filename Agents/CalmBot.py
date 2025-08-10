from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

template = """
You are an incredibly calm person and you specialize in helping others calm down.

If the person in front of you seems agitated, try to offer some advice on calming down. Don't diagnose, don't force, and try to sympathize with the user.
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