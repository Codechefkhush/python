from fastapi import APIRouter, HTTPException
from modules.mathematics import calculate

router = APIRouter(tags= ["Mathematics"], prefix="/mathematics")

@router.get("/calculate")
def calculations(num1: int, num2: int, operation: str = "add"):
    return calculate(num1, num2, operation)
    

@router.get("/addition", summary = "Addition of two numbers")
def addition(num1: float, num2: float):
    return num1 + num2

@router.get("/subtraction", summary = "Subtraction of two numbers")
def subtraction(num1: float, num2: float):
    return num1 - num2

@router.get("/multiplication", summary = "Multiplication of two numbers")
def multiplication(num1: float, num2: float):
    return num1 * num2

@router.get("/division",summary = "Division of two numbers")
def division(num1: float, num2: float):
    if num2 == 0:
        raise HTTPException(status_code=400, detail="num2 cannot be 0.")
    return num1 / num2