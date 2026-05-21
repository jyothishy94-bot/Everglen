"""
Authentication middleware for role-based access control
"""

from fastapi import Request, HTTPException, status
from functools import wraps
from typing import Optional, List
import logging

logger = logging.getLogger(__name__)


class AuthMiddleware:
    """Middleware for authentication and authorization"""

    @staticmethod
    def require_auth(required_roles: Optional[List[str]] = None):
        """Decorator to enforce authentication and role-based access"""
        def decorator(func):
            @wraps(func)
            async def wrapper(request: Request, *args, **kwargs):
                # Extract user info from request (would come from Firebase Auth in production)
                user_id = request.headers.get("X-User-ID")
                user_role = request.headers.get("X-User-Role")

                if not user_id or not user_role:
                    raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="Missing authentication credentials",
                    )

                if required_roles and user_role not in required_roles:
                    raise HTTPException(
                        status_code=status.HTTP_403_FORBIDDEN,
                        detail=f"This endpoint requires one of roles: {', '.join(required_roles)}",
                    )

                # Store user info in request state for downstream handlers
                request.state.user_id = user_id
                request.state.user_role = user_role

                return await func(request, *args, **kwargs)

            return wrapper
        return decorator
