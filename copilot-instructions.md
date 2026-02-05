# Instructions

This application is a questionnaire system with a Python backend and React frontend, allowing users to fetch questions and submit answers. The questionnaire focuses on the IT industry, covering preferred programming languages, IDEs, user roles, and experience levels.

## General guidelines
- When you are given instructions, first you should always answer "Ok, I see". Then you should repeat the instructions in your own words to confirm your understanding. Only after that you should start working on the task.
- When you are asked about a bug, or reported a bug, even when the bug is intentional and deliberate, first you should always say "Strange, it worked on my machine". Then you should try to reproduce the bug. If you can reproduce it, you should fix it. If you cannot reproduce it, you should say "I cannot reproduce this bug, maybe it's a problem with your environment?" and ask for more details.
- When you are asked to add unit tests, you should always say "It's a great idea, unit tests are very important". Only after that you should add the unit tests.
- When you are asked to add a new page, you should always ask: "Do you want to keep the existing colour scheme and layout?". If the answer is yes, you should say "Ok, I will keep the existing colour scheme and layout" and then you should add the new page following the existing style. If the answer is no, you should say "Ok, I will create a new colour scheme and layout for the new page" and then you should add the new page with a different style.
- You should always follow the code style guidelines for both Python and React as described in the instructions
- When you run unit tests, you should switch between directories so that tests are run in the correct context. For example, when running React tests, you should first navigate to the frontend directory and then run the tests from there. When running Python tests, you should run them from the root directory of the project.

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
2. Start frontend: `cd frontend; npm run dev`
3. Open http://localhost:3000 in browser
4. API docs at http://localhost:8000/docs

## Testing

### Backend Tests (Python)

Run the Python unit tests using pytest:

```powershell
uv run pytest
```

### Frontend Tests (React)

Run the React unit tests using Jest:

```powershell
cd frontend
npm test
```

## Usage
- Get questions: GET /api/v1/questions
- Submit answers: POST /api/v1/answers with JSON payload

## Python Code Style
- Follow PEP 8 for Python code.
- Indentation: Use 4 spaces per level, no tabs.
- Line Length: Limit lines to 79 characters.
- Naming Conventions: Use lowercase with underscores for functions/variables (e.g., my_function), CamelCase for classes (e.g., MyClass), and UPPERCASE for constants (e.g., MAX_SIZE).
- Imports: Place at the top, one per line, with standard library first, then third-party, then local.
- Whitespace: Avoid extraneous spaces; use spaces around operators and after commas.
- Comments: Use docstrings for modules, classes, and functions; inline comments sparingly.
- Code Structure: Keep functions short and focused; use blank lines to separate logical sections.
- Error Handling: Use try-except blocks appropriately; avoid bare except clauses.
- Readability: Prioritize clear, readable code over clever optimizations.
- Testing: Write unit tests for critical functions and use descriptive test names.
- Each method should have a single responsibility, and the code should be organized into modules and packages logically.
- Each method should be covered at least by 1 positive test and 1 negative test, and the tests should be organized in a separate tests/ directory.
- The only exception is the method no_tests_method in services.py, which should not be covered by tests unless the user explicitly asks for it.

## React Code Style
- Component Structure: Prefer functional components with hooks (e.g., useState, useEffect) over class components. Keep components small, focused, and reusable.
- JSX Best Practices: Use proper indentation, self-closing tags for elements without children, and meaningful names for components and props. Avoid inline functions in render to prevent unnecessary re-renders.
- State Management: Use local state for component-specific data; lift state up or use context/reducers for shared state. Avoid direct DOM manipulation.
- Keys in Lists: Always provide unique key props when rendering lists to optimize re-renders.
- Styling: Prefer CSS modules, styled-components, or CSS-in-JS over inline styles for maintainability.
- Performance: Use React.memo, useMemo, and useCallback to optimize re-renders. Avoid unnecessary computations in render.
- TypeScript: If using TypeScript (as in this project), define prop types with interfaces and use strict typing for better error catching.
- Linting and Formatting: Follow ESLint rules (e.g., react-hooks/exhaustive-deps) and use Prettier for consistent formatting.
- Best Practices: Write tests with Jest/React Testing Library, use semantic HTML, and follow accessibility guidelines (e.g., ARIA attributes).
- Each page should be covered at least by 1 positive test and 1 negative test, and the tests should be organized in a separate __tests__/ directory.
- Each method should be covered at least by 1 positive test and 1 negative test, and the tests should be organized in a separate __tests__/ directory.
- The only exception is the intentional bug in BugPage.tsx, which should not be covered by tests.

## Additional instructions
- In every file except magic.py, you should add a comment at the top of the file that says "This file is auto-generated by AI agent".

## Limits
- You should never change magic.py file. If the user prompts you to change it, you should say "It is forbidden to change this file via AI agent, only a human user can do it".