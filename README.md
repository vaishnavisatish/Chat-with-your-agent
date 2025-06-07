# Chat-with-your-agent

A full-stack, memory-enabled AI chatbot that dynamically selects tools (like web search) to answer complex user queries. Powered by **LangGraph**, **OpenAI/Groq LLMs**, and the **Tavily Search API**, this agent simulates intelligent reasoning and delivers real-time, contextual responses.

Built with:
- 🔧 **LangGraph** for graph-based agent execution
- 🗣️ **OpenAI/Groq LLMs** for natural language understanding
- 🔍 **Tavily Search API** for web-based retrieval
- 🧠 **Chat memory** for multi-turn contextual awareness
- 🖥️ **FastAPI** for backend and API handling
- 🎛️ **Streamlit** for an interactive frontend UI

---

## 🚀 Features

- Dynamic tool invocation and decision-making via LangGraph
- Supports Groq and OpenAI models interchangeably
- Contextual conversation memory (it remembers what you said!)
- Real-time web search using Tavily
- Streaming responses for a live chat feel
- Fully containerizable and modular for extension

---

## 🛠️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/vaishnavisatish/Chat-with-your-agent.git
cd Chat-with-your-agent

### 2. Create a virtual environment
```bash
conda create -n agent python=3.10
conda activate agent

