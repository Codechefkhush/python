# Python Learning Repository

A personal repo for learning Python — starting with **FastAPI**, a modern web framework for building APIs.

---

## Module 1: FastAPI

### What is FastAPI?

FastAPI is a Python web framework for building HTTP APIs quickly and with minimal code. It is:

- **Fast** — one of the fastest Python frameworks, on par with Node.js and Go
- **Type-safe** — uses Python type hints to validate request/response data automatically
- **Auto-documented** — generates interactive API docs at `/docs` (Swagger UI) and `/redoc` with zero extra work

### Project Structure

```
python/
├── api/
│   ├── __init__.py     # Makes `api` a Python package
│   └── app.py          # FastAPI app and route definitions
├── run.py              # Entry point — starts the server
├── requirements.txt    # Project dependencies
└── README.md
```

---

### Key Concepts

#### 1. The `FastAPI` App Instance

```python
from fastapi import FastAPI

app = FastAPI()
```

`app` is the core object. All routes are registered on it, and it is the object that the server runs.

---

#### 2. Route Decorators

```python
@app.get("/")
def read_root():
    return {"message": "Hello! This is FastAPI"}
```

A **route** maps a URL path and HTTP method to a Python function. The decorator `@app.get("/")` means: _when someone sends a GET request to `/`, call `read_root()`_.

Common HTTP method decorators:

| Decorator        | HTTP Method | Typical Use          |
|------------------|-------------|----------------------|
| `@app.get()`     | GET         | Read / fetch data    |
| `@app.post()`    | POST        | Create new data      |
| `@app.put()`     | PUT         | Update existing data |
| `@app.delete()`  | DELETE      | Delete data          |

FastAPI automatically converts whatever you return from Python dicts/lists into a JSON response.

---

#### 3. Uvicorn — The Server

```python
uvicorn.run("api.app:app", host="0.0.0.0", port=8000, reload=True)
```

**Uvicorn** is an ASGI server — it is the program that actually listens on a network port, receives HTTP requests, and hands them to your FastAPI app.

Think of it like this:

```
Browser / Client
      |
      | HTTP request
      ↓
  Uvicorn (the server)
      |
      | calls
      ↓
  FastAPI app (your code)
      |
      | returns a response
      ↓
  Uvicorn sends it back
      ↓
Browser / Client
```

Key arguments in `uvicorn.run()`:

| Argument | What it does |
|----------|--------------|
| `"api.app:app"` | Points to the `app` object inside `api/app.py` — format is `"module.path:variable"` |
| `host="0.0.0.0"` | Listen on all network interfaces (use `"127.0.0.1"` to restrict to localhost only) |
| `port=8000` | The port number (must be an **integer**, not a string) |
| `reload=True` | Auto-restarts the server when you save a file — great for development |

> **ASGI** (Asynchronous Server Gateway Interface) is the standard that lets async Python web frameworks like FastAPI talk to servers like Uvicorn.

---

#### 4. `__init__.py`

The empty file `api/__init__.py` tells Python that the `api` folder is a **package** — meaning you can import from it using `from api.app import app`. Without this file, the import would fail.

---

### Running the App

**Step 1 — Install dependencies:**

```bash
pip install -r requirements.txt
```

**Step 2 — Start the server:**

```bash
python run.py
```

**Step 3 — Open in browser:**

- API: [http://localhost:8000](http://localhost:8000)
- Interactive docs: [http://localhost:8000/docs](http://localhost:8000/docs)
- Alternative docs: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

### Bug Fixes Made (Learning Notes)

| File | Bug | Fix |
|------|-----|-----|
| `run.py` | `port="8000"` — port was a string | Changed to `port=8000` (integer) |
| `run.py` | Folder named `fastapi/` shadowed the installed `fastapi` library | Renamed folder to `api/` |
| `run.py` | Import `from fastapi.app import app` failed | Changed to `from api.app import app` |
| `requirements.txt` | Was empty | Added `fastapi` and `uvicorn[standard]` |

> **Why does folder name matter?** Python searches for modules by name. If your folder is called `fastapi`, Python finds it first when you write `from fastapi import FastAPI` — and since your folder doesn't define `FastAPI`, the import fails. Always avoid naming your folders/files the same as installed packages.

---

### What's Next

- Path parameters: `/items/{item_id}`
- Query parameters: `/items?skip=0&limit=10`
- Request body with Pydantic models
- Async route handlers with `async def`
- Dependency injection
