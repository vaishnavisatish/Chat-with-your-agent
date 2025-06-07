# Optional: Load environment variables manually if not using pipenv
# from dotenv import load_dotenv
# load_dotenv()

# Step 1: Define the data schema for incoming requests
from pydantic import BaseModel
from typing import List

class ChatRequest(BaseModel):
    provider: str
    model: str
    prompt: str
    messages: List[str]
    enable_search: bool


# Step 2: Setup FastAPI application and route
from fastapi import FastAPI
from ai_agent import query_agent

SUPPORTED_MODELS = [
    "llama3-70b-8192",
    "llama-3.3-70b-versatile",
    "gpt-4o-mini"
]

app = FastAPI(title="AI Agent Service with LangGraph")

@app.post("/chat")
def handle_chat(req: ChatRequest):
    """
    Handle chat requests using the LangGraph agent framework.
    Allows selection of models and optional search tool usage.
    """
    if req.model not in SUPPORTED_MODELS:
        return {"error": "Selected model is not supported. Please choose a valid option."}

    # Extract fields from request
    response = query_agent(
        model_name=req.model,
        user_input=req.messages,
        search_enabled=req.enable_search,
        prompt=req.prompt,
        backend=req.provider
    )
    return {"response": response}


# Step 3: Run with Uvicorn (or use Swagger UI at /docs for testing)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=9999)
