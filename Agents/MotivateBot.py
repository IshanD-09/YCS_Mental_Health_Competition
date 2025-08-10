
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

# Prompt template for a therapist-style agent
template = """
You are a life coach who specializes in motivating young people (high schoolers and young adults) to pursue their passions or to accomplish their goals. 
Conversation so far:
{chat_history}

User: {user_input}

Respond in a way that boosts their confidence or supports them emotionally.
"""

# Set up prompt + LLM + chain once
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

    # result might be a dictionary with 'text' or 'content'
    if isinstance(result, dict):
        return result.get("text") or result.get("content") or str(result)
    
    # fallback in case of a direct string or unexpected format
    return str(result)