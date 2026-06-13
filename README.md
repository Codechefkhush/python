# Python Learning — Concepts Reference

A reference document covering the core Python and FastAPI concepts explored in this tutorial repository.

---

## Python Concepts

### Type Hints

Python is dynamically typed, but since Python 3.5 you can annotate variables and function parameters with types. These are not enforced by Python itself at runtime, but tools like FastAPI and Pydantic use them to validate data automatically.

```python
def greet(name: str) -> str:
    return "Hello " + name
```

### Modules and Packages

A **module** is any `.py` file. A **package** is a folder containing an `__init__.py` file, which tells Python to treat that folder as an importable module. You import from them using dot notation — `from api.math import router`.

### Functions as First-Class Objects

In Python, functions are objects. You can pass them around, store them in variables, and use them as arguments. Decorators (like `@app.get("/")`) rely on this — they are functions that wrap other functions to add behaviour.

---

## FastAPI Concepts

### What is FastAPI?

FastAPI is a modern Python web framework for building HTTP APIs. It is built on top of **Starlette** (for the web layer) and **Pydantic** (for data validation), and it uses Python type hints to do most of the heavy lifting automatically.

### ASGI

ASGI (Asynchronous Server Gateway Interface) is the standard interface between async Python web frameworks and web servers. FastAPI is an ASGI framework, which is why it needs an ASGI server like Uvicorn to run.

### Uvicorn

Uvicorn is the web server that runs your FastAPI application. It listens on a port, receives HTTP requests, and passes them to your app. It supports `reload=True` for development, which restarts the server automatically whenever you save a file.

### The App Instance

`FastAPI()` creates the main application object. Everything — routes, routers, middleware — is registered on this object. It is the entry point that Uvicorn receives requests from.

### Routes and HTTP Methods

A route maps a URL path and an HTTP method to a Python function. FastAPI supports all standard HTTP methods:

- **GET** — retrieve data; no request body
- **POST** — send data to create or process something; supports a request body
- **PUT** — update an existing resource
- **DELETE** — remove a resource

Using the wrong method (e.g. GET when you need to send a body) is a common mistake — GET requests do not carry a body, so Pydantic models must be used with POST or PUT.

### Path Parameters

A variable segment in the URL, defined with curly braces. FastAPI extracts it and passes it as a function argument.

```python
@app.get("/user/{name}")
def get_user(name: str): ...
```

### Query Parameters

Parameters passed in the URL after a `?`. Any function parameter that is not a path parameter is automatically treated as a query parameter.

```python
@app.get("/calculate")
def calculate(a: float, b: float): ...
# called as /calculate?a=10&b=5
```

### Request Body and Pydantic

When you need to send structured data to an endpoint (like a form or JSON payload), you define a Pydantic `BaseModel`. FastAPI reads the request body, validates it against the model, and gives you a Python object.

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
```

Pydantic also raises clear validation errors automatically if the data doesn't match the schema.

### APIRouter

`APIRouter` lets you split your routes across multiple files and then register them all on the main app with `app.include_router()`. Each router can have a `prefix` (e.g. `/mathematics`) and `tags` to group routes in Swagger UI.

### Auto-generated Documentation

FastAPI automatically generates two interactive API documentation pages with zero configuration:

- **Swagger UI** — available at `/docs`
- **ReDoc** — available at `/redoc`

These are built from the route definitions, type hints, and `summary` strings you write. Tags (from `APIRouter`) are used to group routes into sections in the Swagger UI.

---

## Modules Covered

| Module | Concepts Practised |
|--------|-------------------|
| FastAPI Basics | App instance, GET routes, path parameters |
| Mathematics Router | APIRouter, prefix, tags, query parameters |
| Validator Router | POST routes, Pydantic models, importing from external modules |
