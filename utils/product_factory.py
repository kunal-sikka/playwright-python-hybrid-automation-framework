from datetime import datetime


def build_product() -> dict:
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
    return {
        "name": f"Auto{timestamp[-10:]}",
        "category": "fashion",
        "sub_category": "shirts",
        "price": "1200",
        "description": "Automation portfolio test product",
        "product_for": "men",
    }
