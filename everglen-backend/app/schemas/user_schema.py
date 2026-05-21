"""
Pydantic schemas for user authentication and registration
"""

from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime


class PhoneOTPRequest(BaseModel):
    """Schema for sending OTP to phone number"""
    phone_number: str = Field(..., regex=r'^\+?91[6-9]\d{9}$', description="Valid Indian phone number")

    class Config:
        schema_extra = {
            "example": {
                "phone_number": "+919876543210"
            }
        }


class VerifyOTPRequest(BaseModel):
    """Schema for verifying OTP"""
    phone_number: str = Field(..., regex=r'^\+?91[6-9]\d{9}$')
    otp_code: str = Field(..., regex=r'^\d{6}$', description="6-digit OTP")

    class Config:
        schema_extra = {
            "example": {
                "phone_number": "+919876543210",
                "otp_code": "123456"
            }
        }


class CustomerRegistrationRequest(BaseModel):
    """Schema for customer registration"""
    phone_number: str = Field(..., regex=r'^\+?91[6-9]\d{9}$')
    full_name: str = Field(..., min_length=3, max_length=100)
    email: Optional[EmailStr] = None

    class Config:
        schema_extra = {
            "example": {
                "phone_number": "+919876543210",
                "full_name": "John Doe",
                "email": "john@example.com"
            }
        }


class HotelRegistrationRequest(BaseModel):
    """Schema for hotel/kitchen registration"""
    phone_number: str = Field(..., regex=r'^\+?91[6-9]\d{9}$')
    hotel_name: str = Field(..., min_length=3, max_length=100)
    category: str = Field(..., regex=r'^(restaurant|home_kitchen|cloud_kitchen|cafe)$')
    address: str = Field(..., min_length=10)
    city: str = Field(..., min_length=2)
    postal_code: str = Field(..., regex=r'^\d{6}$')
    fssai_license_number: str = Field(..., regex=r'^\d{14}$', description="14-digit FSSAI number")
    pan_number: Optional[str] = Field(None, regex=r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$')
    gstin: Optional[str] = Field(None, regex=r'^\d{2}[A-Z]{5}\d{4}[A-Z]{1}[A-Z\d]{3}$')
    latitude: float
    longitude: float

    class Config:
        schema_extra = {
            "example": {
                "phone_number": "+919876543210",
                "hotel_name": "The Golden Fork",
                "category": "restaurant",
                "address": "123 Main Street, Downtown",
                "city": "Bangalore",
                "postal_code": "560001",
                "fssai_license_number": "10012345678901",
                "latitude": 12.9716,
                "longitude": 77.5946
            }
        }


class DriverRegistrationRequest(BaseModel):
    """Schema for driver registration"""
    phone_number: str = Field(..., regex=r'^\+?91[6-9]\d{9}$')
    full_name: str = Field(..., min_length=3, max_length=100)
    driving_license_number: str = Field(..., min_length=10)
    vehicle_registration_number: str = Field(..., min_length=8)
    onboarding_path: str = Field(..., regex=r'^(upfront_500|installment_600)$')

    class Config:
        schema_extra = {
            "example": {
                "phone_number": "+919876543210",
                "full_name": "Raj Kumar",
                "driving_license_number": "DL0120170012345",
                "vehicle_registration_number": "KA01AB1234",
                "onboarding_path": "upfront_500"
            }
        }


class UserResponse(BaseModel):
    """Schema for user profile response"""
    user_id: str
    phone_number: str
    full_name: str
    role: str
    email: Optional[str] = None
    is_verified: bool
    created_at: datetime
    is_active: bool

    class Config:
        from_attributes = True


class TokenResponse(BaseModel):
    """Schema for authentication token response"""
    access_token: str
    token_type: str = "bearer"
    user: UserResponse
    expires_in: int
