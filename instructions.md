# Instructions

## Prerequisites
- Python 3.11+
- Node.js 18+
- uv package manager

## Setup
1. Install uv: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
2. Install dependencies: `uv sync`
3. Install frontend dependencies: `cd frontend && npm install`

## Running the Application
1. Start backend: `uv run uvicorn src.main:app --reload --host 0.0.0.0 --port 8000`
2. Start frontend: `cd frontend && npm run dev`
3. Open http://localhost:3000 in browser
4. API docs at http://localhost:8000/docs

## Usage
- Get questions: GET /api/v1/questions
- Submit answers: POST /api/v1/answers with JSON payload