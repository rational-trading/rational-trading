from typing import Optional
from ninja.security import HttpBearer
from django.http.request import HttpRequest

from config.env import env
import jwt


class AuthBearer(HttpBearer):
    def authenticate(self, request: HttpRequest, token: str) -> Optional[str]:
        try:
            # JWT secret key is set up in ../config/.env
            JWT_SIGNING_KEY: str = env("JWT_SIGNING_KEY")
            payload = jwt.decode(token, JWT_SIGNING_KEY, algorithms=[
                                 "HS256"])
            username: Optional[str] = payload.get("sub")
            return username
        except jwt.PyJWTError as e:
            return None
