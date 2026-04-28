from datetime import datetime

import pytest

from api.auth_client import AuthClient
from api.orders_client import OrdersClient
from api.products_client import ProductsClient
from api.workflows import EcommerceApiWorkflow
from config.settings import load_settings
from utils.credentials import get_credentials


def _sanitize_nodeid(nodeid: str) -> str:
    return (
        nodeid.replace("/", "_")
        .replace("\\", "_")
        .replace("::", "__")
        .replace("[", "_")
        .replace("]", "")
    )


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="qa",
        help="Test environment defined in config/environments.json",
    )
    parser.addoption(
        "--browser_name",
        action="store",
        default="chromium",
        choices=["chromium", "chrome", "firefox", "webkit"],
        help="Browser selection",
    )
    parser.addoption(
        "--viewport-width",
        action="store",
        type=int,
        default=1440,
        help="Browser viewport width",
    )
    parser.addoption(
        "--viewport-height",
        action="store",
        type=int,
        default=900,
        help="Browser viewport height",
    )

@pytest.fixture(scope="session")
def settings(request):
    return load_settings(request.config.getoption("env"))


@pytest.fixture(scope="session")
def browser_name(request):
    return request.config.getoption("browser_name")


@pytest.fixture(scope="session")
def headed(request):
    return request.config.getoption("headed")


@pytest.fixture(scope="session")
def viewport(request):
    return {
        "width": request.config.getoption("viewport_width"),
        "height": request.config.getoption("viewport_height"),
    }


@pytest.fixture(scope="session")
def user_credentials():
    credentials = get_credentials()
    return {
        "userEmail": credentials["email"],
        "userPassword": credentials["password"],
    }


@pytest.fixture
def bdd_context():
    return {}


@pytest.fixture
def auth_client(playwright, settings):
    client = AuthClient(playwright, settings)
    yield client
    client.dispose()


@pytest.fixture
def orders_client(playwright, settings):
    client = OrdersClient(playwright, settings)
    yield client
    client.dispose()


@pytest.fixture
def products_client(playwright, settings):
    client = ProductsClient(playwright, settings)
    yield client
    client.dispose()


@pytest.fixture
def api_workflow(playwright, settings):
    workflow = EcommerceApiWorkflow(playwright, settings)
    yield workflow
    workflow.dispose()


@pytest.fixture
def page(playwright, browser_name, headed, viewport, request):
    if browser_name in ["chromium", "chrome"]:
        browser = playwright.chromium.launch(headless=not headed)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=not headed)
    else:
        browser = playwright.webkit.launch(headless=not headed)

    context = browser.new_context(viewport=viewport)
    page = context.new_page()
    request.node.page = page
    yield page
    context.close()
    browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or not report.failed:
        return

    page = getattr(item, "page", None)
    if page is None or page.is_closed():
        return

    screenshots_dir = item.config.rootpath / "test-results" / "screenshots"
    screenshots_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path = screenshots_dir / f"{_sanitize_nodeid(item.nodeid)}_{timestamp}.png"
    page.screenshot(path=str(screenshot_path), full_page=True)
