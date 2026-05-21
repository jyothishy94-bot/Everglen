# API Documentation

## Base URL
```
http://localhost:8000
```

## Interactive Documentation
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

---

## Authentication Endpoints

### Send OTP to Phone Number
```http
POST /auth/send-otp
Content-Type: application/json

{
  "phone_number": "+919876543210"
}
```

**Response (200 OK):**
```json
{
  "status": "success",
  "message": "OTP sent successfully",
  "expires_in": 600
}
```

---

### Verify OTP and Login
```http
POST /auth/verify-otp
Content-Type: application/json

{
  "phone_number": "+919876543210",
  "otp_code": "123456"
}
```

**Response (200 OK):**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "bearer",
  "user": {
    "user_id": "user_12345",
    "phone_number": "+919876543210",
    "full_name": "John Doe",
    "role": "customer",
    "email": "john@example.com",
    "is_verified": true,
    "created_at": "2026-05-21T15:00:00Z",
    "is_active": true
  },
  "expires_in": 1800
}
```

---

## Customer Registration Endpoints

### Register New Customer
```http
POST /auth/register-customer
Content-Type: application/json

{
  "phone_number": "+919876543210",
  "full_name": "John Doe",
  "email": "john@example.com"
}
```

**Response (201 Created):**
```json
{
  "status": "success",
  "message": "Customer registered successfully",
  "user_id": "customer_12345"
}
```

---

## Hotel Registration Endpoints

### Register New Hotel/Kitchen
```http
POST /auth/register-hotel
Content-Type: application/json

{
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
```

**Response (201 Created):**
```json
{
  "status": "success",
  "message": "Hotel registered successfully",
  "hotel_id": "hotel_12345",
  "next_step": "Upload FSSAI document"
}
```

---

## Driver Registration Endpoints

### Register New Driver
```http
POST /auth/register-driver
Content-Type: application/json

{
  "phone_number": "+919876543210",
  "full_name": "Raj Kumar",
  "driving_license_number": "DL0120170012345",
  "vehicle_registration_number": "KA01AB1234",
  "onboarding_path": "upfront_500"
}
```

**Response (201 Created):**
```json
{
  "status": "success",
  "message": "Driver registered successfully",
  "driver_id": "driver_12345",
  "next_step": "Complete onboarding payment"
}
```

---

## Order Endpoints

### Create New Order
```http
POST /orders
Authorization: Bearer {access_token}
Content-Type: application/json

{\n  \"hotel_id\": \"hotel_12345\",\n  \"menu_items\": [\n    {\n      \"item_id\": \"item_1\",\n      \"item_name\": \"Biryani\",\n      \"quantity\": 2,\n      \"base_price\": 250.0,\n      \"subtotal\": 500.0\n    }\n  ],\n  \"delivery_address\": {\n    \"street\": \"123 Main Street\",\n    \"city\": \"Bangalore\",\n    \"postal_code\": \"560001\",\n    \"latitude\": 12.9716,\n    \"longitude\": 77.5946\n  },\n  \"payment_method\": \"cash\"\n}\n```\n\n**Response (201 Created):**\n```json\n{\n  \"order_id\": \"order_12345\",\n  \"customer_id\": \"customer_12345\",\n  \"hotel_id\": \"hotel_12345\",\n  \"food_cost\": 500.0,\n  \"delivery_charge\": 50.0,\n  \"platform_fee\": 5.0,\n  \"total_amount\": 555.0,\n  \"status\": \"pending\",\n  \"created_at\": \"2026-05-21T15:00:00Z\"\n}\n```\n\n---\n\n### Get Order Details\n```http\nGET /orders/{order_id}\nAuthorization: Bearer {access_token}\n```\n\n**Response (200 OK):**\n```json\n{\n  \"order_id\": \"order_12345\",\n  \"customer_id\": \"customer_12345\",\n  \"hotel_id\": \"hotel_12345\",\n  \"driver_id\": \"driver_12345\",\n  \"food_cost\": 500.0,\n  \"delivery_charge\": 50.0,\n  \"platform_fee\": 5.0,\n  \"total_amount\": 555.0,\n  \"status\": \"out_for_delivery\",\n  \"created_at\": \"2026-05-21T15:00:00Z\",\n  \"updated_at\": \"2026-05-21T15:30:00Z\"\n}\n```\n\n---\n\n### Update Order Status\n```http\nPATCH /orders/{order_id}/status\nAuthorization: Bearer {access_token}\nContent-Type: application/json\n\n{\n  \"status\": \"preparing\",\n  \"notes\": \"Order is being prepared\"\n}\n```\n\n**Response (200 OK):**\n```json\n{\n  \"status\": \"success\",\n  \"message\": \"Order status updated\",\n  \"new_status\": \"preparing\"\n}\n```\n\n---\n\n## Wallet Endpoints\n\n### Get Wallet Balance\n```http\nGET /drivers/{driver_id}/wallet\nAuthorization: Bearer {access_token}\n```\n\n**Response (200 OK):**\n```json\n{\n  \"driver_id\": \"driver_12345\",\n  \"current_balance\": 1250.0,\n  \"total_topups\": 2000.0,\n  \"total_deductions\": 750.0,\n  \"is_locked\": false,\n  \"last_transaction_at\": \"2026-05-21T15:30:00Z\",\n  \"updated_at\": \"2026-05-21T15:30:00Z\"\n}\n```\n\n---\n\n### Top-up Wallet (UPI)\n```http\nPOST /drivers/{driver_id}/wallet/topup\nAuthorization: Bearer {access_token}\nContent-Type: application/json\n\n{\n  \"amount\": 500.0,\n  \"payment_method\": \"upi\"\n}\n```\n\n**Response (200 OK):**\n```json\n{\n  \"status\": \"success\",\n  \"message\": \"Wallet top-up initiated\",\n  \"transaction_id\": \"txn_12345\",\n  \"amount\": 500.0,\n  \"new_balance\": 1750.0\n}\n```\n\n---\n\n### Get Wallet Transaction History\n```http\nGET /drivers/{driver_id}/wallet/transactions?limit=10&offset=0\nAuthorization: Bearer {access_token}\n```\n\n**Response (200 OK):**\n```json\n{\n  \"transactions\": [\n    {\n      \"transaction_id\": \"txn_12345\",\n      \"driver_id\": \"driver_12345\",\n      \"transaction_type\": \"deduction\",\n      \"amount\": 5.0,\n      \"balance_before\": 1255.0,\n      \"balance_after\": 1250.0,\n      \"order_id\": \"order_12345\",\n      \"description\": \"Platform fee for order\",\n      \"created_at\": \"2026-05-21T15:30:00Z\"\n    }\n  ],\n  \"total\": 150,\n  \"limit\": 10,\n  \"offset\": 0\n}\n```\n\n---\n\n## Hotel Endpoints\n\n### Get Hotel Profile\n```http\nGET /hotels/{hotel_id}\nAuthorization: Bearer {access_token}\n```\n\n**Response (200 OK):**\n```json\n{\n  \"hotel_id\": \"hotel_12345\",\n  \"hotel_name\": \"The Golden Fork\",\n  \"category\": \"restaurant\",\n  \"status\": \"active\",\n  \"rating\": 4.8,\n  \"total_orders\": 152,\n  \"address\": \"123 Main Street, Downtown\",\n  \"city\": \"Bangalore\",\n  \"latitude\": 12.9716,\n  \"longitude\": 77.5946,\n  \"is_onboarding_fee_paid\": true,\n  \"created_at\": \"2026-05-21T15:00:00Z\"\n}\n```\n\n---\n\n### Get Nearby Hotels\n```http\nGET /hotels/nearby?latitude=12.9716&longitude=77.5946&radius=5\nAuthorization: Bearer {access_token}\n```\n\n**Response (200 OK):**\n```json\n{\n  \"hotels\": [\n    {\n      \"hotel_id\": \"hotel_12345\",\n      \"hotel_name\": \"The Golden Fork\",\n      \"category\": \"restaurant\",\n      \"rating\": 4.8,\n      \"distance_km\": 1.2,\n      \"latitude\": 12.9716,\n      \"longitude\": 77.5946\n    }\n  ],\n  \"total\": 42\n}\n```\n\n---\n\n## Error Responses\n\n### 401 Unauthorized\n```json\n{\n  \"detail\": \"Invalid or expired token\",\n  \"error_code\": \"UNAUTHORIZED\"\n}\n```\n\n### 403 Forbidden\n```json\n{\n  \"detail\": \"You do not have permission to access this resource\",\n  \"error_code\": \"FORBIDDEN\"\n}\n```\n\n### 404 Not Found\n```json\n{\n  \"detail\": \"Order not found\",\n  \"error_code\": \"NOT_FOUND\"\n}\n```\n\n### 400 Bad Request (Validation Error)\n```json\n{\n  \"detail\": \"Validation error\",\n  \"error_code\": \"VALIDATION_ERROR\",\n  \"data\": {\n    \"field\": \"phone_number\",\n    \"message\": \"Invalid phone number format\"\n  }\n}\n```\n\n---\n\n## Status Codes\n\n- `200 OK` - Request successful\n- `201 Created` - Resource created successfully\n- `400 Bad Request` - Invalid request data\n- `401 Unauthorized` - Missing or invalid authentication\n- `403 Forbidden` - Insufficient permissions\n- `404 Not Found` - Resource not found\n- `409 Conflict` - Resource already exists\n- `500 Internal Server Error` - Server error\n"
  