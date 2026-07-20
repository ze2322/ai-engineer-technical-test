from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from section4_deployment.models import (
    ChatRequest,
    ChatResponse,
)

from section4_deployment.ollama_service import (
    OllamaService,
)

app = FastAPI(
    title="Electro Pi AI API"
)

ollama = OllamaService()


@app.get("/")
def home():

    return {
        "status": "running"
    }


@app.post("/generate")

def generate(
    request: ChatRequest,
):

    answer = ollama.generate(
        request.prompt
    )

    return ChatResponse(
        response=answer
    )


@app.post("/stream")
def stream(
    request: ChatRequest,
):

    def generator():

        answer = ollama.generate(
            request.prompt
        )

        for word in answer.split():

            yield word + " "

    return StreamingResponse(
        generator(),
        media_type="text/plain",
    )