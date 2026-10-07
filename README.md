# 🚀 Enterprise E-Commerce E2E Automation Framework

A robust, scalable, and production-ready test automation framework built to test an E-Commerce application end-to-end. This framework bridges Backend API testing and Frontend UI automation into a single, cohesive CI/CD pipeline.

## 🛠️ Tech Stack & Tools
* **Automation Tool:** Playwright (Python)
* **Test Runner:** PyTest
* **Backend API Integration:** Python requests & json
* **Test Data Generation:** Faker Library & Dynamic Timestamps
* **Design Pattern:** Page Object Model (POM)
* **CI/CD Pipeline:** GitHub Actions

## 🏗️ Framework Architecture & Core Features

* **Hybrid Data-Driven Approach:** Fetches real user JSON data dynamically via a REST API (reqres.in) and seamlessly injects it into the UI Registration and Checkout flows.
* **Collision-Free Data:** Implemented time.time() timestamps combined with API data to generate 100% unique user credentials per test run, effectively eliminating database duplication errors.
* **Page Object Model (POM):** Strict separation of element locators and actions (Pages) from the actual test logic (Tests) for maximum reusability and low maintenance.
* **Environment Variable Management:** Secure management of Base URLs and API Endpoints using .env files locally and GitHub Repository Secrets in the cloud pipeline.
* **Continuous Integration:** Fully automated .yml workflow that triggers headless test execution on Ubuntu cloud runners for every push to the main branch.
* **Automated Reporting:** Generates comprehensive HTML test execution reports via pytest-html.

## ⚙️ Local Setup & Execution

1. Clone the repository:
git clone https://github.com/tarunparihar079-glitch/Playwright-Python-E2E-Framework.git
cd Playwright-Python-E2E-Framework

2. Install dependencies:
pip install -r requirements.txt

3. Set up Environment Variables:
Create a .env file in the root directory and add the following:
LT_URL=[https://ecommerce-playground.lambdatest.io/](https://ecommerce-playground.lambdatest.io/)
REQRES_API_URL=[https://reqres.in/api/users/](https://reqres.in/api/users/)

4. Run Tests (Headed Mode with slow motion):
pytest tests/test_lt_e2e.py -s --headed --slowmo 1000

5. Run Tests (Headless Mode for CI/CD):
pytest tests/test_lt_e2e.py --html=report.html