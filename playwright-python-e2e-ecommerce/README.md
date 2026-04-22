# GreenKart E2E Automation - Playwright & Python

This repository contains an End-to-End (E2E) automation test suite for the **GreenKart** practice platform. The primary goal is to validate the shopping flow, cart management, and product data integrity using **Playwright** and **Python**.

## Source
Exercise inspired by a Python course on Udemy and using the practice page: https://rahulshettyacademy.com/practice

## 🚀 Technologies Used

* **Language:** Python 3.x
* **Test Framework:** Pytest
* **Automation Tool:** Playwright
* **Documentation Style:** BDD (Gherkin) via test comments.

## 🛠️ Key Project Features

* **Auto-retrying Assertions:** Leveraged Playwright's `expect` library to handle site latency and eliminate "flaky" tests.
* **Modularity:** Implemented reusable functions for data scraping and product manipulation.
* **Dynamic Validation:** Real-time calculation of product totals (Price * Quantity) comparing the catalog vs. the cart view.
* **Clean Code:** Structured to follow DRY (Don't Repeat Yourself) principles and prepared for Page Object Model (POM) transition.

## 📋 Automated Scenarios

Tests are documented using the **Gherkin** format and include:
1. **Empty Cart Validation:** Verifies initial state, warning messages, and empty state imagery.
2. **Element Integrity:** Ensures added items display correct images, names, prices, and action buttons.
3. **Data Synchronization:** Validates that catalog information matches cart data exactly after interaction.
4. **Product Removal:** Confirms the cart updates correctly when items are deleted.
5. **Batch Testing:** High-volume validation of multiple products with different quantities simultaneously.

Note: This implementation improves upon standard examples by utilizing Playwright's auto-waiting mechanism and dynamic data validation between the catalog and the checkout preview.

## 🔧 Installation and Execution

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/green-kart-automation.git](https://github.com/YOUR_USERNAME/green-kart-automation.git)
   cd green-kart-automation
   
2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    
4. **Install Playwright browsers:**
   ```bash
   playwright install

5. **Run test:**
   ```bash
   # Run all tests in headed mode
    pytest --headed
   
   # Run and generate an HTML report
    pytest --html=report.html

## 📂 Installation and Execution
 1. test_green_cart.py: Contains the test scripts.
 2. requirements.txt: Project dependendy list.
 3. .gitignore: Files explided from version control.
 
## 🎓 Credits & Attribution

This project was inspired by the automation exercises from **Rahul Shetty Academy**. While the test scenarios are based on their practice platform, the **technical solution, architecture, and code implementation** (including the transition to Playwright-native assertions and modular functions) were designed and developed entirely by me as part of my learning journey.

