from typing import Optional
from ninja.security import HttpBearer
from django.http.request import HttpRequest

from dotenv import load_dotenv
import jwt
import os


class AuthBearer(HttpBearer):
    def authenticate(self, request: HttpRequest, token: str) -> Optional[str]:
        try:
            # JWT secret key is set up in .env
            load_dotenv()
            JWT_SIGNING_KEY = os.getenv(JWT_SIGNING_KEY)
            payload = jwt.decode(token, JWT_SIGNING_KEY, algorithms=["HS256"])
            username: str = payload.get("sub")
            if username is None:
                return None
        except jwt.PyJWTError as e:
            return None
        return username
