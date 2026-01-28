from typing import Optional, List
from pydantic import BaseModel
import httpx
import os

# Simplified representation of the LLM strategy
# We'll support OpenRouter for cloud bursts and vLLM for local speed.

class LLMRequest(BaseModel):
    prompt: str
    model_provider: str = "openrouter" # or "local"
    model_name: str
    temperature: float = 0.0

class LLMProvider:
    def __init__(self):
        self.openrouter_key = os.getenv("OPENROUTER_API_KEY")
        
    async def generate(self, request: LLMRequest):
        if request.model_provider == "local":
            return await self._generate_local(request)
        else:
            return await self._generate_openrouter(request)

    async def _generate_openrouter(self, request: LLMRequest):
        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.openrouter_key}",
            "HTTP-Referer": "https://github.com/datht-react/Javis",
            "Content-Type": "application/json"
        }
        data = {
            "model": request.model_name,
            "messages": [{"role": "user", "content": request.prompt}],
            "temperature": request.temperature
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, json=data, timeout=60.0)
            return response.json()

    async def _generate_local(self, request: LLMRequest):
        # This will interface with the vLLM engine logic from run_inference.py
        # Placeholder for actual async vLLM call
        return {"choices": [{"message": {"content": f"LOCAL MODEL ({request.model_name}) RESPONSE: [Not yet connected to running vLLM process]"}}]}
