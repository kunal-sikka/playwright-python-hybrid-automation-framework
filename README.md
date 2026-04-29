# 🚀 Playwright Python Hybrid Automation Framework (UI + API + BDD)

![CI](https://github.com/kunal-sikka/playwright-python-hybrid-automation-framework/actions/workflows/tests.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.12-blue)
![Playwright](https://img.shields.io/badge/playwright-tested-green)
![Pytest](https://img.shields.io/badge/pytest-framework-orange)
![BDD](https://img.shields.io/badge/bdd-pytest--bdd-yellow)
![Allure](https://img.shields.io/badge/reporting-allure-purple)

---

## 📌 Overview

This is a **production-style hybrid automation framework** built using Playwright (Python), Pytest, and BDD.

It demonstrates a **modern QA strategy** where:

- API is used for **fast test setup**
- UI is used for **end-to-end validation**
- BDD is used for **business-readable scenarios**

👉 Designed to reflect how real-world QA teams build **scalable and reliable automation systems**

---

## ⚡ Key Highlights

- Hybrid testing (**API + UI validation**)
- Clean **Page Object Model (POM)** architecture
- Dedicated **API client layer** (Auth, Orders)
- Reusable **workflow layer for E2E setup**
- **BDD implementation** using pytest-bdd
- Secure credential handling (**.env + GitHub Secrets**)
- Automatic **failure screenshots**
- **Allure reporting** with readable steps
- **CI/CD pipeline** with GitHub Actions
- Retry mechanism for flaky network/API calls

---

## 🛠 Tech Stack

- Python 3.12
- Playwright (UI + API)
- Pytest
- pytest-bdd
- Allure Reports
- GitHub Actions

---

## 🧠 Architecture Approach

The framework follows **separation of concerns**:

- `pages/` → UI interactions (POM)
- `api/` → Backend API layer
- `workflows/` → Hybrid orchestration logic
- `tests/` → UI, API, and E2E tests
- `features/` → BDD scenarios

👉 Result: **clean, maintainable, scalable automation design**

---

## 📁 Project Structure
.
├── api/
│   ├── assertions.py          # API response validations
│   ├── auth_client.py         # Authentication API client
│   ├── orders_client.py       # Orders API client
│   ├── products_client.py     # Products API client
│   └── workflows.py           # Hybrid API workflows
│
├── config/
│   ├── environments.json      # Environment configs (QA, etc.)
│   ├── settings.py            # Config loader & models
│   └── test_data.py           # Static test data
│
├── data/
│   └── credentials.example.json   # Sample credentials structure
│
├── docs/
│   └── QA_Test_Suite_Hybrid_Playwright_Framework.xlsx   # Test documentation
│
├── features/                  # BDD feature files
│   ├── api_order.feature
│   ├── cart.feature
│   ├── checkout.feature
│   ├── hybrid_order.feature
│   ├── login.feature
│   └── order_history.feature
│
├── pages/                     # Page Object Model (UI)
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── confirmation_page.py
│   ├── dashboard_page.py
│   ├── login_page.py
│   ├── order_details_page.py
│   ├── order_history_page.py
│   └── register_page.py
│
├── tests/
│   ├── step_definitions/      # BDD step implementations
│   │   ├── test_api_order_steps.py
│   │   ├── test_cart_steps.py
│   │   ├── test_checkout_steps.py
│   │   ├── test_hybrid_order_steps.py
│   │   ├── test_login_steps.py
│   │   └── test_order_history_steps.py
│   │
│   ├── test_api_auth.py
│   ├── test_api_order_flow.py
│   ├── test_api_order_negative.py
│   ├── test_api_product_flow.py
│   ├── test_api_security.py
│   ├── test_cart_flow.py
│   ├── test_checkout_flow.py
│   ├── test_e2e_flow.py
│   ├── test_login_flow.py
│   ├── test_order_flow.py
│   └── test_registration_flow.py
│
├── utils/
│   ├── credentials.py         # Env-based credential handling
│   ├── product_factory.py     # Test data generator
│   └── user_factory.py        # User data factory
│
├── .github/
│   └── workflows/
│       └── tests.yml          # CI pipeline
│
├── conftest.py                # Pytest fixtures
├── pytest.ini                 # Pytest configuration
├── requirements.txt           # Dependencies
├── README.md
├── .gitignore


---

## ⚙️ Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install

---

🔐 Environment Setup

Create a .env file in the root:

TEST_EMAIL=your-email@example.com
TEST_PASSWORD=your-password

.env is not committed for security
GitHub CI uses repository secrets

---

▶️ Running Tests

pytest
pytest --env=qa
pytest -m api
pytest -m ui
pytest -m e2e
pytest -m bdd
pytest --browser_name=firefox
pytest --headed

---

🔁 BDD Coverage

BDD scenarios validate business flows such as:

Login
Add to cart
Checkout
API order creation
API-created order visible in UI
Order history validation

Example:
Feature: Login

  Scenario: User logs in with valid credentials
    Given login user is on the login page
    When login user logs in with valid credentials
    Then login user should see the products page

---

🔄 CI/CD Pipeline
Runs on every push & pull request
Executes full test suite
Uses secure GitHub Secrets
Uploads:
Allure results
Failure screenshots
Includes retry for flaky tests

---

📊 Reporting

Allure report provides:

Feature-based grouping
Step-level execution logs
Business-readable test flows

To generate locally:

pytest --alluredir=allure-results
allure serve allure-results

---

🔥 Flagship Hybrid Flow

This project demonstrates a real-world high-value scenario:

Generate login token via API
Create order via API
Login via UI
Navigate to order history
Validate API-created order in UI

👉 Reduces UI dependency and speeds up E2E testing significantly

---

🤖 AI-Assisted Development

This framework leverages tools like Codex and Claude to enhance productivity:

Accelerated framework setup and refactoring
Improved code quality and structure
Faster debugging and issue resolution

👉 AI was used as a productivity accelerator, while all architecture, validation logic, and QA decisions were designed and verified manually

---

💼 Why This Project Matters

This project showcases:

Real-world QA automation architecture
Hybrid testing strategy (API + UI)
Scalable and maintainable design
CI/CD readiness
Strong QA engineering practices

👉 Built to reflect skills directly applicable to production environments and client projects

---

📬 Contact

If you're interested in collaborating or discussing QA automation opportunities, feel free to connect.
