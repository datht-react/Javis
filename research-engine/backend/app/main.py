from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from app.core.llm_provider import LLMProvider, LLMRequest
import uvicorn

app = FastAPI(title="Javis Research Engine API")

# Enable CORS for the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

llm = LLMProvider()

class SearchRequest(BaseModel):
    query: str
    model_provider: str = "openrouter"
    model_name: str = "google/gemini-2.0-flash-001" # Default SOTA for speed

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/search")
async def conduct_research(request: SearchRequest):
    # 1. Search Logic (Placeholder for web_search/Tavily)
    search_context = f"Context found for: {request.query}" 
    
    # 2. Synthesize with LLM
    prompt = f"""
    You are Javis, an AI Research Assistant.
    Research Query: {request.query}
    Search Results: {search_context}
    
    Synthesize a technical answer with citations.
    """
    
    llm_req = LLMRequest(
        prompt=prompt,
        model_provider=request.model_provider,
        model_name=request.model_name
    )
    
    response = await llm.generate(llm_req)
    return {
        "answer": response.get("choices", [{}])[0].get("message", {}).get("content", "Error generating response"),
        "sources": [{"title": "Initial Search Result", "url": "https://arxiv.org"}]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
