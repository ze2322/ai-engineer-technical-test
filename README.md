# Electro Pi AI Engineer Technical Test

# NOTE: Work Not Completed
- STT and TTS are stubbed due to the absence of a compatible local provider in the current environment.
- GPU-based 4-bit benchmarking could not be executed because CUDA hardware was unavailable.
- Benchmark results were collected on CPU and therefore do not represent GPU inference performance.
- Full concurrent load testing was not performed.

## Overview

This repository contains my solution for the **Electro Pi AI Engineer Technical Test**.

The project demonstrates practical AI engineering skills across four sections:

- **Section 1:** LiveKit AI Agent
- **Section 2:** Retrieval-Augmented Generation (RAG)
- **Section 3:** LLM Quantization & Benchmarking
- **Section 4:** FastAPI Deployment & Docker

The implementation focuses on clean, modular, and maintainable code while using open-source tools whenever possible.

---

# Environment

- Python 3.12
- Windows 11
- Docker Desktop
- Ollama
- LiveKit Cloud
- FastAPI

---

# Technologies Used

- Python
- LiveKit Agents SDK
- Ollama
- LangChain
- Hugging Face Transformers
- Sentence Transformers
- FAISS
- FastAPI
- Docker
- PyTorch

---

# Project Structure

```
.
├── section1_livekit/
├── section2_rag/
├── section3_quantization/
├── section4_deployment/
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/ze2322/ai-engineer-technical-test.git

cd electro-pi-ai-test
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Section 1 — LiveKit AI Agent

## Features

- LiveKit Agents Python SDK
- AgentSession
- Custom Agent
- Local Ollama LLM
- Tool Calling
- System Prompt
- LiveKit Cloud Worker

Run

```bash
python -m section1_livekit.main
```

### Implementation Notes

The project uses the **LiveKit Agents Python SDK** together with a **local Ollama LLM**.

The assignment allows Speech-to-Text (STT) and Text-to-Speech (TTS) components to be stubbed or mocked when provider keys or external services are unavailable, provided that the LLM and agent logic are implemented correctly.

Due to the absence of a fully local STT/TTS provider compatible with the current environment, the voice pipeline is partially stubbed. The project architecture remains compatible with LiveKit's STT → LLM → TTS workflow and can be extended with supported STT and TTS providers without modifying the agent logic.

---

# Section 2 — Retrieval-Augmented Generation (RAG)

## Features

- Document Loading
- Text Chunking
- Sentence Transformer Embeddings
- FAISS Vector Database
- Similarity Search
- Source Citations
- Context-aware Responses

Run

```bash
python section2_rag/main.py
```

Example Questions

- What is Artificial Intelligence?
- Explain Docker.
- Explain Retrieval-Augmented Generation.
- What are Transformers?

---

# Section 3 — Model Quantization & Benchmarking

## Model

```
Qwen/Qwen2.5-1.5B-Instruct
```

Run

```bash
python section3_quantization/fp16.py
```

Results are saved to

```
section3_quantization/output/
```

The benchmark records:

- Latency
- Generated Tokens
- Tokens per Second
- Memory Usage

### Implementation Notes

The benchmark was executed on **CPU** because the development machine does not provide CUDA-enabled GPU support.

The repository includes the quantization implementation; however, GPU-based 4-bit benchmarking could not be executed in the current environment due to hardware limitations.

The FP32/CPU benchmark demonstrates the benchmarking workflow and performance evaluation.

---

# Section 4 — FastAPI Deployment

## Features

- REST API
- Streaming Endpoint
- Swagger Documentation
- Docker Support

Run locally

```bash
uvicorn section4_deployment.api:app --reload
```

Swagger UI

```
http://localhost:8000/docs
```

---

# Docker

Build

```bash
docker build -t electro-pi-ai .
```

Run

```bash
docker run -p 8000:8000 electro-pi-ai
```

Open Swagger

```
http://localhost:8000/docs
```

---

# API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | API Check |
| POST | `/generate` | Generate Response |
| POST | `/stream` | Streaming Response |

---

# Performance Notes

A simple latency measurement was performed during API testing by measuring inference response times.

The deployment supports streaming responses through FastAPI.

Full concurrent load testing (e.g., Locust, k6, or ApacheBench) was not performed due to time and hardware constraints.

---

# Assumptions

- Ollama is installed locally.
- The required LLM is available in Ollama.
- Docker Desktop is installed.
- Internet access is available when using LiveKit Cloud.
- CUDA-enabled GPU hardware was not available during development.

---
