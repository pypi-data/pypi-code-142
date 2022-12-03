import os

BIND_END_POINT = os.environ.get(
    "BIND_END_POINT", "https://sandbox.bind.com.ar/v1/"
)  # sandbox
BIND_USER = os.environ.get("BIND_USER", "gus@gmail.com")
BIND_PASSWORD = os.environ.get("BIND_PASSWORD", "aaskdqweqweqw")
REDIS_CONNECTION = os.environ.get("REDIS_CONNECTION", False)
BANK_ID = os.environ.get("BANK_ID", 322)
VIEW_ID = os.environ.get("VIEW_ID", "owner")
