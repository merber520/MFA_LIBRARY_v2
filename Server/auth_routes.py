#api routes for authentication

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# Data models
class PasswordValidationRequest(BaseModel):
    password: str
    hashed_password: str

class OTPValidationRequest(BaseModel):
    otp: str
    secret_key: str

@router.post("/validate-password")
async def validate_password(request: PasswordValidationRequest):
    # Placeholder for validation logic
    return {"success": True, "message": "Password validated successfully."}

@router.post("/validate-otp")
async def validate_otp(request: OTPValidationRequest):
    # Placeholder for OTP validation logic
    return {"success": True, "message": "OTP validated successfully."}
