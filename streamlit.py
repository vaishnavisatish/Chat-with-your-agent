import streamlit as st
import requests

# ---------------- Sidebar Configuration ----------------
st.set_page_config(page_title="Conversational AI Agent", layout="wide")

with st.sidebar:
    st.title("⚙️ Agent Configuration")

    provider_choice = st.radio("Model Provider", ("Groq", "OpenAI"))

    groq_models = ["llama-3.3-70b-versatile"]
    openai_models = ["gpt-4o-mini"]

    model_choice = st.selectbox(
        "Select Model",
        groq_models if provider_choice == "Groq" else openai_models
    )

    agent_description = st.text_area(
        "System Prompt",
        placeholder="Describe how the agent should behave...",
        height=100
    )

    enable_search = st.checkbox("Enable Web Search")

    st.markdown("---")
    st.caption("Customize your AI agent and interact via the chat window.")

# ---------------- Chat State ----------------
st.title("💬 AI Chat Interface")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---------------- User Input ----------------
user_input = st.text_input("You:", placeholder="Type your question and press Enter...")

backend_url = "http://127.0.0.1:9999/chat"

# ---------------- Send Request & Display Response ----------------
def send_query():
    if not user_input.strip():
        return

    # Append user query to chat history
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    payload = {
        "model": model_choice,
        "provider": provider_choice,
        "prompt": agent_description,
        "messages": [entry["content"] for entry in st.session_state.chat_history if entry["role"] == "user"],
        "enable_search": enable_search
    }

    try:
        response = requests.post(backend_url, json=payload)
        response_data = response.json()

        if "error" in response_data:
            st.session_state.chat_history.append({"role": "error", "content": response_data["error"]})
        else:
            st.session_state.chat_history.append({"role": "agent", "content": response_data["response"]})

    except Exception as e:
        st.session_state.chat_history.append({"role": "error", "content": f"Backend Error: {e}"})


if user_input:
    send_query()

# ---------------- Display Chat History ----------------
st.markdown("### 🧠 Conversation")
for message in st.session_state.chat_history:
    if message["role"] == "user":
        st.markdown(f"**You:** {message['content']}")
    elif message["role"] == "agent":
        st.markdown(f"**Agent:** {message['content']}")
    elif message["role"] == "error":
        st.error(message["content"])
