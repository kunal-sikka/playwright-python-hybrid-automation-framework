from datetime import datetime


def build_registered_user() -> dict:
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
    return {
        "first_name": "Portfolio",
        "last_name": "User",
        "email": f"portfolio.user.{timestamp}@example.com",
        "mobile": "9876543210",
        "occupation": "Engineer",
        "gender": "Male",
        "password": "Portfolio@123",
    }
