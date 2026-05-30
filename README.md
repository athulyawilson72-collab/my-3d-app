# 3D Model Generator

A web application that generates 3D models from natural language prompts using OpenSCAD and Mistral AI.

## API Endpoints (Base URL: http://127.0.0.1:8000)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Health check |
| POST | /generate | Text prompt → 3D model (PNG) |
| POST | /refine | Modify existing model |
| POST | /route | Classify prompt: parametric or ai_generator |
| GET | /download/stl | Download STL file |

## Tech Stack
- Backend: FastAPI + Python
- AI: Mistral AI
- 3D Engine: OpenSCAD
- Frontend: Next.js + Tailwind + Three.js

## Run Locally
```bash
uvicorn api:app --reload
```