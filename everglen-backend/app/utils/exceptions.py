"""
Custom exception classes for Everglen API
"""

from fastapi import HTTPException
from typing import Optional, Dict, Any


class EverglenException(HTTPException):
    """Base exception for Everglen API"""

    def __init__(
        self,
        status_code: int,
        detail: str,
        error_code: Optional[str] = None,
        data: Optional[Dict[str, Any]] = None,
    ):
        self.status_code = status_code
        self.detail = detail
        self.error_code = error_code
        self.data = data or {}
        super().__init__(status_code=status_code, detail=detail)


class UnauthorizedException(EverglenException):
    """401 Unauthorized"""

    def __init__(self, detail: str = "Unauthorized", error_code: str = "UNAUTHORIZED"):
        super().__init__(status_code=401, detail=detail, error_code=error_code)


class ForbiddenException(EverglenException):
    """403 Forbidden"""

    def __init__(self, detail: str = "Forbidden", error_code: str = "FORBIDDEN"):
        super().__init__(status_code=403, detail=detail, error_code=error_code)


class NotFoundException(EverglenException):
    """404 Not Found"""

    def __init__(self, detail: str = "Resource not found", error_code: str = "NOT_FOUND"):
        super().__init__(status_code=404, detail=detail, error_code=error_code)


class ConflictException(EverglenException):
    """409 Conflict"""

    def __init__(self, detail: str = "Resource already exists", error_code: str = "CONFLICT"):
        super().__init__(status_code=409, detail=detail, error_code=error_code)


class ValidationException(EverglenException):
    """400 Bad Request - Validation Error"""

    def __init__(self, detail: str = "Validation error", error_code: str = "VALIDATION_ERROR", data: Optional[Dict] = None):
        super().__init__(status_code=400, detail=detail, error_code=error_code, data=data)


class FirebaseException(EverglenException):
    """500 Internal Server Error - Firebase Error"""

    def __init__(self, detail: str = "Firebase operation failed", error_code: str = "FIREBASE_ERROR"):
        super().__init__(status_code=500, detail=detail, error_code=error_code)


class OTPException(EverglenException):
    """OTP-related errors"""

    def __init__(self, detail: str = "OTP verification failed", error_code: str = "OTP_ERROR"):
        super().__init__(status_code=400, detail=detail, error_code=error_code)


class InsufficientWalletException(EverglenException):
    """Insufficient wallet balance"""

    def __init__(self, detail: str = "Insufficient wallet balance", error_code: str = "INSUFFICIENT_BALANCE"):
        super().__init__(status_code=400, detail=detail, error_code=error_code)


class WalletLockedException(EverglenException):
    """Wallet is locked"""

    def __init__(self, detail: str = "Wallet is locked", error_code: str = "WALLET_LOCKED", reason: Optional[str] = None):
        data = {"reason": reason} if reason else {}
        super().__init__(status_code=403, detail=detail, error_code=error_code, data=data)
