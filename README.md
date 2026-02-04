# Questionnaire API

A simple questionnaire API built with FastAPI, following clean architecture principles. The application allows users to retrieve questions and submit answers through a RESTful API.

## Features

- **Clean Architecture**: Organized into domain, application, infrastructure, and presentation layers
- **FastAPI**: Modern, fast web framework with automatic OpenAPI documentation
- **Swagger UI**: Interactive API documentation at `/docs`
- **JSON File Storage**: Answers are stored in JSON files in the 'answers' directory (persistent across restarts)
- **JSON Configuration**: Questions loaded from `config/questions.json`
- **Type Safety**: Full type hints with Pydantic models

## Project Structure

```
1_02_Homework/
├── src/                    # Backend (Python/FastAPI)
│   ├── domain/              # Business entities and repository interfaces
│   │   ├── models.py
│   │   └── repositories.py
│   ├── application/         # Business logic and services
│   │   └── services.py
│   ├── infrastructure/      # Repository implementations
│   │   └── repositories.py
│   ├── presentation/        # API routes and controllers
│   │   └── routes.py
│   └── main.py             # Application entry point
├── frontend/               # Frontend (React/TypeScript)
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── services/        # API service layer
│   │   ├── types/           # TypeScript types
│   │   └── main.tsx         # Frontend entry point
│   ├── package.json
│   └── vite.config.ts
├── config/
│   └── questions.json      # Questions configuration
├── .vscode/
│   └── launch.json         # VS Code debug configuration
├── pyproject.toml          # Python dependencies
└── README.md
```

## Prerequisites

- Python 3.11 or higher
- [uv](https://github.com/astral-sh/uv) package manager
- Node.js 18+ and npm (for frontend)

### Windows PowerShell Execution Policy

If you encounter an error like "execution of scripts is disabled on this system" when running npm commands, you need to change the PowerShell execution policy.

**Run PowerShell as Administrator and execute:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Type `Y` to confirm. This is a one-time setup that allows running npm scripts.

**Alternative**: Use Command Prompt (cmd.exe) instead of PowerShell to run npm commands.

## Installation

1. **Install uv** (if not already installed):
```powershell
# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

2. **Install dependencies**:
```powershell
uv sync
```

## Usage

### Running the Full Application (Backend + Frontend)

**Step 1: Start the Backend Server**

Open a terminal and run:
```powershell
uv run uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

Or use VS Code debugger (Press `F5` and select "Python: FastAPI")

The backend API will be available at:
- **API Base URL**: http://localhost:8000
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

**Step 2: Start the Frontend Development Server**

Open a new terminal, navigate to the frontend directory, and run:
```powershell
cd frontend
npm install   # First time only
npm run dev
```

The frontend will be available at:
- **Web UI**: http://localhost:3000

**Important**: Both backend and frontend must be running simultaneously. The frontend proxies API requests to the backend on port 8000.

### API Endpoints

#### 1. GET /api/v1/questions
Retrieve all available questions from the questionnaire.

**Example Request:**
```bash
curl http://localhost:8000/api/v1/questions
```

**Example Response:**
```json
[
  {
    "id": "q1",
    "text": "What is your name?",
    "type": "text",
    "options": null
  },
  {
    "id": "q2",
    "text": "What is your favorite programming language?",
    "type": "multiple_choice",
    "options": ["Python", "JavaScript", "Java", "C#", "Go", "Rust", "Other"]
  }
]
```

#### 2. POST /api/v1/answers
Submit answers to the questionnaire. Answers are stored in JSON files.

**Example Request:**
```bash
curl -X POST http://localhost:8000/api/v1/answers \
  -H "Content-Type: application/json" \
  -d '{
    "answers": [
      {"question_id": "q1", "answer": "John Doe"},
### Using the Application

**Web Interface (Recommended)**
1. Open http://localhost:3000 in your browser
2. Fill out all questions in the form
3. Click "Submit Answers" button
4. See the success message
5. Optionally submit another response

**Swagger UI (API Testing)**
1. Navigate to http://localhost:8000/docs
2. You'll see all available endpoints with full documentation
3. Click on any endpoint to expand it
4. Click "Try it out" to test the endpoint
5. Fill in parameters (if any) and click "Execute"
6. View the response
  "message": "Answers submitted successfully",
  "count": 2
}
```

### Using Swagger UI

1. Navigate to http://localhost:8000/docs
2. You'll see all available endpoints with full documentation
3. Click on any endpoint to expand it
4. Click "Try it out" to test the endpoint
5. Fill in parameters (if any) and click "Execute"
6. View the response

## Development

### Debug Configuration

The project includes VS Code debug configurations in `.vscode/launch.json`:

- **Python: FastAPI** - Start the FastAPI server with debugging
- **Python: Current File** - Debug the currently open Python file

To start debugging:
1. Set breakpoints in your code
2. Press `F5` or click Run → Start Debugging
3. Select "Python: FastAPI"
4. Make API requests to trigger breakpoints

### Modifying Questions

Edit `config/questions.json` to add, remove, or modify questions:

```json
{
  "questions": [
    {
      "id": "q1",
      "text": "Your question here?",
      "type": "text",
      "options": null
    }
  ]
}
```

Question types:
- `text`: Free text input
- `multiple_choice`: Select from predefined options

### Architecture Layers

**Domain Layer** (`src/domain/`):
- Core business entities (Question, Answer)
- Repository interfaces
- No external dependencies

**Application Layer** (`src/application/`):
- Business logic and use cases
- Service classes that orchestrate operations
- Depends only on domain layer

**Infrastructure Layer** (`src/infrastructure/`):
- Concrete implementations of repositories
- External concerns (file I/O, databases, etc.)
- Implements domain interfaces

**Presentation Layer** (`src/presentation/`):
- API routes and HTTP concerns
- Request/response handling
- Depends on application layer

## Notes

- Answers are stored in JSON files in the 'answers' directory and persist across server restarts
- The application uses CORS middleware to allow cross-origin requests
- All endpoints are prefixed with `/api/v1` for versioning
- Health check endpoints available at `/` and `/health`

## License

MIT
