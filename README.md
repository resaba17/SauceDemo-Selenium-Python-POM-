# SauceDemo Selenium Automation Testing

## Project Overview
This project is an automated testing framework developed using Python, Selenium WebDriver, and Pytest. It automates the testing of the SauceDemo e-commerce application by following the Page Object Model (POM) design pattern.

## Application Under Test
https://www.saucedemo.com/

## Technologies Used
- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- Git
- GitHub
- Visual Studio Code

## Project Structure
```
EcommerceAutomation/
│
├── pages/
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   └── menu_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_invalid_login.py
│   ├── test_logout.py
│   ├── test_random_products.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   ├── test_sort.py
│   ├── test_product_validation.py
│   └── test_reset_app.py
│
├── utils/
├── reports/
├── screenshots/
├── requirements.txt
├── pytest.ini
└── README.md
```

## Test Cases
- Valid Login
- Invalid Login
- Logout
- Random Product Validation
- Add Product to Cart
- Cart Verification
- Checkout Process
- Product Sorting
- Product Validation
- Reset App State

## Installation

Clone the repository:

```bash
git clone https://github.com/resaba17/SauceDemo-Selenium-Python-POM-.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Execute Tests

Run all test cases:

```bash
python -m pytest -v
```

## Framework
- Selenium WebDriver
- Pytest
- Page Object Model (POM)

## Author
**Resaba**
