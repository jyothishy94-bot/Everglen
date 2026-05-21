"""
Pydantic schemas for order management
"""

from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class MenuItemRequest(BaseModel):
    """Schema for menu items in order"""
    item_id: str
    item_name: str
    quantity: int = Field(..., ge=1)
    base_price: float = Field(..., gt=0)
    subtotal: float = Field(..., gt=0)


class AddressRequest(BaseModel):
    """Schema for delivery/pickup address"""
    street: str = Field(..., min_length=5)
    city: str = Field(..., min_length=2)
    postal_code: str = Field(..., regex=r'^\d{6}$')
    latitude: Optional[float] = None
    longitude: Optional[float] = None


class CreateOrderRequest(BaseModel):
    """Schema for creating a new order"""
    hotel_id: str
    menu_items: List[MenuItemRequest]
    delivery_address: AddressRequest
    special_instructions: Optional[str] = None
    payment_method: str = Field(default="cash", regex=r'^(cash|upi)$')

    class Config:
        schema_extra = {
            "example": {
                "hotel_id": "hotel_123",
                "menu_items": [
                    {
                        "item_id": "item_1",
                        "item_name": "Biryani",
                        "quantity": 2,
                        "base_price": 250.0,
                        "subtotal": 500.0
                    }
                ],
                "delivery_address": {
                    "street": "123 Main Street",
                    "city": "Bangalore",
                    "postal_code": "560001",
                    "latitude": 12.9716,
                    "longitude": 77.5946
                },
                "payment_method": "cash"
            }
        }


class OrderStatusUpdateRequest(BaseModel):
    """Schema for updating order status"""
    status: str = Field(
        ...,
        regex=r'^(pending|accepted_by_kitchen|preparing|ready_for_pickup|picked_up_by_driver|out_for_delivery|delivered|cancelled)$'
    )
    notes: Optional[str] = None


class OrderResponse(BaseModel):
    """Schema for order response"""
    order_id: str
    customer_id: str
    hotel_id: str
    driver_id: Optional[str] = None
    food_cost: float
    delivery_charge: float
    platform_fee: float = 5.0
    total_amount: float
    status: str
    created_at: datetime
    updated_at: datetime
    completed_at: Optional[datetime] = None

    class Config:
        from_attributes = True
