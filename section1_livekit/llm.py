from livekit.plugins import openai

from section1_livekit.config import (
    OLLAMA_MODEL,
    OLLAMA_BASE_URL,
)

llm = openai.LLM(
    model=OLLAMA_MODEL,
    api_key="ollama",
    base_url=OLLAMA_BASE_URL,
)