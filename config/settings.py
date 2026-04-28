import json
from dataclasses import dataclass
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
ENVIRONMENTS_FILE = PROJECT_ROOT / "config" / "environments.json"


@dataclass(frozen=True)
class OrderSettings:
    country: str
    product_ordered_id: str


@dataclass(frozen=True)
class Settings:
    env: str
    base_url: str
    client_path: str
    default_order: OrderSettings

    @property
    def client_base_url(self) -> str:
        return f"{self.base_url}{self.client_path}"

    @property
    def login_url(self) -> str:
        return f"{self.client_base_url}/"

    @property
    def registration_url(self) -> str:
        return f"{self.client_base_url}/#/auth/register"

    @property
    def orders_url(self) -> str:
        return f"{self.client_base_url}/#/dashboard/myorders"

    @property
    def default_order_payload(self) -> dict:
        return {
            "orders": [
                {
                    "country": self.default_order.country,
                    "productOrderedId": self.default_order.product_ordered_id,
                }
            ]
        }


def load_settings(env: str) -> Settings:
    with open(ENVIRONMENTS_FILE, encoding="utf-8") as file:
        environments = json.load(file)

    if env not in environments:
        supported_envs = ", ".join(sorted(environments))
        raise ValueError(f"Unsupported env '{env}'. Supported envs: {supported_envs}")

    env_config = environments[env]
    order_config = env_config["default_order"]

    return Settings(
        env=env,
        base_url=env_config["base_url"],
        client_path=env_config.get("client_path", "/client"),
        default_order=OrderSettings(
            country=order_config["country"],
            product_ordered_id=order_config["product_ordered_id"],
        ),
    )
