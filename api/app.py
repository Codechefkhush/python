from fastapi import FastAPI
from api.mathematics import router as math_router
from api.validator import router as validator_router

app = FastAPI()

app.include_router(math_router)
app.include_router(validator_router)

@app.get("/")
def read_root():
    return {"message": "Hello! Welcome to python tutorial."}
