# Hybrid UI + API Automation Framework with Playwright Python

Production-style test automation framework demonstrating hybrid end-to-end validation with Playwright, Pytest, and Pytest-BDD.

## Tech Stack

- Python
- Playwright
- Pytest
- Pytest-BDD
- Allure Report
- Playwright APIRequestContext
- Page Object Model
- Domain-based API clients

## What This Framework Demonstrates

- API-driven test data setup before UI validation
- Dedicated API clients for authentication and order workflows
- Reusable hybrid workflow layer for E2E setup
- Page Object Model for reusable UI actions
- Pytest fixtures for browser lifecycle management
- Configurable viewport and headed/headless execution
- Screenshot capture on UI test failure
- API-only and hybrid E2E coverage
- Data-driven E2E tests
- BDD scenario coverage for business-readable flows
- Cross-browser execution through CLI options
- Allure results with features, stories, severity, titles, and business-readable steps
- GitHub Actions pipeline with test artifact upload

## Project Structure

```text
.
├── api/
│   ├── assertions.py
│   ├── auth_client.py
│   ├── orders_client.py
│   └── workflows.py
├── config/
│   ├── environments.json
│   ├── settings.py
│   └── test_data.py
├── data/
│   └── credentials.example.json
├── docs/
│   └── test_cases.md
├── features/
│   ├── api_order.feature
│   ├── cart.feature
│   ├── checkout.feature
│   ├── hybrid_order.feature
│   ├── login.feature
│   └── order_history.feature
├── pages/
│   ├── dashboard_page.py
│   ├── login_page.py
│   ├── order_details_page.py
│   ├── order_history_page.py
│   └── register_page.py
├── .github/
│   └── workflows/
│       └── tests.yml
├── conftest.py
├── pytest.ini
├── requirements.txt
├── tests/
│   ├── step_definitions/
│   └── test_*.py
```

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install
```

## 🔐 Environment Setup

Live tests require valid demo application credentials through environment variables. Credentials are never read from committed files.

macOS/Linux:

```bash
export TEST_EMAIL="your-email@example.com"
export TEST_PASSWORD="your-password"
```

Windows PowerShell:

```powershell
$env:TEST_EMAIL="your-email@example.com"
$env:TEST_PASSWORD="your-password"
```

Optional local `.env` support:

```text
TEST_EMAIL=your-email@example.com
TEST_PASSWORD=your-password
```

For GitHub Actions, add repository secrets named `TEST_EMAIL` and `TEST_PASSWORD`.

## Configuration

Environment-level values are managed in `config/environments.json`:

- base application URL
- client application path
- default order country
- default product ID used for API order creation

The default environment is `qa`.

## Run Tests

```bash
pytest
pytest --env=qa
pytest -m api
pytest -m bdd
pytest -m e2e
pytest --browser_name=firefox
pytest --headed
pytest --viewport-width=1920 --viewport-height=1080
```

## BDD Test Coverage

BDD scenarios live in `features/`, with step definitions in `tests/step_definitions/`.

Covered BDD flows:

- valid login
- add product to cart
- checkout/place order
- API order creation
- API-created order visible in UI
- order history validation

Run BDD tests:

```bash
pytest tests/step_definitions
pytest -m bdd
pytest --alluredir=allure-results
```

Sample scenario:

```gherkin
Feature: Login

  Scenario: User logs in with valid credentials
    Given login user is on the login page
    When login user logs in with valid credentials
    Then login user should see the products page
```

Pytest writes Allure result files to:

```text
allure-results/
```

The Allure report groups coverage by:

- API Validation
- UI Validation
- Hybrid E2E
- BDD Hybrid E2E

Each test includes business-readable steps such as authentication, API order creation, UI login, order history navigation, and final order detail validation.

To generate and open a local Allure report, install the Allure command-line tool, then run:

```bash
allure serve allure-results
```

## Failure Artifacts

Failed tests that use the framework `page` fixture automatically capture a full-page screenshot:

```text
test-results/screenshots/
```

## CI/CD

GitHub Actions runs the Playwright Pytest suite on push, pull request, and manual dispatch.

The workflow uploads:

- `allure-results/`
- `test-results/screenshots/`

Live credentials are intentionally not committed. Configure these GitHub repository secrets to run live tests in CI:

- `TEST_EMAIL`
- `TEST_PASSWORD`

Without local credentials or configured CI secrets, tests fail fast with a clear setup error.

## Current Flagship Scenario

1. Login token is generated using the API.
2. Order is created through the API.
3. User logs in through the UI.
4. User navigates to order history.
5. UI verifies the API-created order details page.

## Portfolio Notes

This project is designed to showcase practical QA automation skills that clients care about: faster E2E setup, reduced UI flakiness, reusable page objects, and clear test organization.
