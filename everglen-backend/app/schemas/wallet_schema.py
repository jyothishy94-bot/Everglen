"""
Pydantic schemas for wallet and financial operations
"""

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class WalletTopupRequest(BaseModel):
    """Schema for wallet top-up request"""
    amount: float = Field(..., gt=0, description="Amount to top-up in INR")
    payment_method: str = Field(default="upi", regex=r'^(upi|card|netbanking)$')

    class Config:
        schema_extra = {
            "example": {
                "amount": 500.0,
                "payment_method": "upi"
            }
        }


class WalletResponse(BaseModel):
    """Schema for wallet status response"""
    driver_id: str
    current_balance: float
    total_topups: float
    total_deductions: float
    is_locked: bool
    lock_reason: Optional[str] = None
    last_transaction_at: Optional[datetime] = None
    updated_at: datetime

    class Config:
        from_attributes = True


class WalletTransactionResponse(BaseModel):
    """Schema for wallet transaction history"""
    transaction_id: str
    driver_id: str
    transaction_type: str
    amount: float
    balance_before: float
    balance_after: float
    order_id: Optional[str] = None
    description: str
    created_at: datetime

    class Config:
        from_attributes = True


class InstallmentPlanResponse(BaseModel):
    """Schema for installment plan status"""
    driver_id: str
    total_amount: float = 600.0
    weekly_installment: float = 150.0
    total_weeks: int = 4
    weeks_paid: int
    amount_paid: float
    amount_remaining: float
    is_active: bool
    next_due_date: Optional[datetime] = None
    updated_at: datetime

    class Config:
        from_attributes = True
