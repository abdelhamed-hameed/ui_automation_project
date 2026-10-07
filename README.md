# 🖥️ UI Automation Testing Framework (Playwright)

A robust and scalable UI testing framework built with **Python**, **Playwright**, and **Pytest**, utilizing the **Page Object Model (POM)** design pattern for maintainable and readable test code.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Testing Framework:** Pytest
- **Browser Automation:** Playwright (Chromium)
- **Design Pattern:** Page Object Model (POM)
- **Reporting:** Allure Report
- **Target Application:** [SauceDemo](https://www.saucedemo.com/) (E-commerce test site)

## ✨ Features
- ✅ Automated UI tests for login (valid/invalid) and shopping cart functionalities.
- ✅ Implementation of Page Object Model (POM) for clean separation of test logic and page elements.
- ✅ Automatic waiting mechanisms (`wait_for_selector`) to eliminate flaky tests.
- ✅ Professional HTML test reports with step-by-step execution details via Allure.

## 📋 Prerequisites
1. **Python 3.x** 
2. **Playwright** (`pip install playwright` && `playwright install chromium`)
3. **Java JDK 17+** & **Allure Commandline** (For reporting)

## ⚙️ Installation & Setup

1. Clone this repository:
   ```bash
   git clone <your-repository-url>
   cd ui_automation_project