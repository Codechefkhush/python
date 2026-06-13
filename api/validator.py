from fastapi import APIRouter
from pydantic import BaseModel
from modules.password_checker import password_validator as validate_password

router = APIRouter(prefix="/validator", tags=["Validator"])

class PasswordValidator(BaseModel):
    password: str
    
@router.post("/", summary = "This check the strength of password")
def password_validator(data: PasswordValidator):
    password = data.password
    return validate_password(password)