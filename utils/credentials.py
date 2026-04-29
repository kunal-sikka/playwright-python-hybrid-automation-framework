import os

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None


class MissingCredentialsError(RuntimeError):
    pass


def get_credentials() -> dict:
    if load_dotenv:
        load_dotenv(override=True)

    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")

    if not email or not password:
        raise MissingCredentialsError(
            "Missing TEST_EMAIL or TEST_PASSWORD environment variables. "
            "Set them before running tests."
        )

    return {"email": email, "password": password}
