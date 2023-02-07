from ninja.security import HttpBearer


class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        # Auth stuff (e.g. JWT) can go here.
        if token == "supersecret":
            return "user123"
        else:
            return None
