from typing import Optional
from ninja.security import HttpBearer
from django.http.request import HttpRequest


class AuthBearer(HttpBearer):
    def authenticate(self, request: HttpRequest, token: str) -> Optional[str]:
        # Auth stuff (e.g. JWT) can go here.
        if token == "supersecret":
            return "user123"
        else:
            return None
