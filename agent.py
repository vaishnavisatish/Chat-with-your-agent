import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

# Load environment variables from .env file
load_dotenv()

# Retrieve API keys from environment
groq_key = os.getenv("GROQ_API_KEY")
openai_key = os.getenv("OPENAI_API_KEY")
tavily_key = os.getenv("TAVILY_API_KEY")

# Initialize models
groq_model = ChatGroq(model="llama-3.3-70b-versatile")
openai_model = ChatOpenAI(model="gpt-4o-mini")
default_prompt = "Act as a chatbot without hallucinations"

def query_agent(model_name, user_input, search_enabled, prompt, backend):
    """Query the appropriate AI agent with or without search tool."""
    if backend == "Groq":
        llm_instance = ChatGroq(model=model_name)
    elif backend == "OpenAI":
        llm_instance = ChatOpenAI(model=model_name)
    else:
        raise ValueError(f"Unsupported provider: {backend}")

    search_tools = [TavilySearchResults(max_results=3)] if search_enabled else []

    agent_executor = create_react_agent(
        model=llm_instance,
        tools=search_tools,
        state_modifier=prompt
    )

    input_state = {"messages": user_input}
    result = agent_executor.invoke(input_state)

    # Extract the last AI message
    dialogue = result.get("messages", [])
    replies = [msg.content for msg in dialogue if isinstance(msg, AIMessage)]

    return replies[-1] if replies else "No response generated."
