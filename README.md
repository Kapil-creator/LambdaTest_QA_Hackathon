
# 🧪 QA Hackathon Framework — Powered by Python, Pytest & LambdaTest 🚀

## 🧪 Test Scenarios & LambdaTest Test IDs

### 🔐 **Login Scenarios Build**

| Test Case       | Description     | LambdaTest Test ID |
|-----------------|------------------|---------------------|
| ✅ Valid Login   | Login with correct credentials | `YD8RW-VJKYV-RXXEE-HU4KK` |
| ❌ Invalid Login | Login with wrong credentials   | `0JLJ5-DK9FM-RHWI8-T5ILQ` |

---

### 🔔 **JS Alerts Scenarios Build**

| Test Case         | Description                  | LambdaTest Test ID |
|-------------------|------------------------------|---------------------|
| JS Alert          | Accept simple alert          | `MJOIZ-UTRAN-WLXP2-VMXPZ` |
| JS Confirm OK     | Accept confirmation alert    | `R0XOJ-QAFOS-GAYIG-QDOC6` |
| JS Confirm Cancel | Dismiss confirmation alert   | `CTHKO-OFJU2-WUCCA-SOYOP` |
| JS Prompt Input   | Send text in prompt alert    | `JY3RR-UXP8T-72XOW-BT7M5` |
| JS Prompt Cancel  | Cancel prompt alert          | `F3LNQ-DV4FA-D5UP4-C4ANN` |

---

## 🧠 Thought Process

I built this framework keeping **real-world QA needs** in mind — ensuring it's **robust, scalable, and reusable** for any web application. I followed industry best practices to address **each evaluation criterion** by:

- Structuring code using the **Page Object Model (POM)** for reusability.
- Leveraging **Pytest** for flexible and powerful test execution.
- Using **`.env`** to protect sensitive credentials and environment config.
- Adding **parallel execution** to reduce execution time.
- Enabling **reruns for flaky tests** to ensure stability.
- Generating **clean HTML reports** for visibility and tracking.
- Integrating with **LambdaTest** for cloud-based, cross-browser testing.

Each test is executed remotely with LambdaTest and has a unique Test ID for reference.

---

## ✅ Evaluation Criteria & How It's Achieved

| Criteria | Achieved? | How |
|---------|-----------|-----|
| **Solid framework creation** | ✅ | Modular, reusable with `pages/`, `utils/`, and POM |
| **Dependency management** | ✅ | All dependencies listed in `requirements.txt` |
| **Test libraries** | ✅ | Built using `pytest`, supports fixtures and plugins |
| **Parallel execution** | ✅ | `pytest-xdist` allows `-n` to run tests concurrently |
| **Re-running failed cases** | ✅ | Using `pytest-rerunfailures` plugin |
| **Clean logs + reports** | ✅ | HTML reports generated via `pytest-html` |
| **Secure credential handling** | ✅ | `.env` file and `dotenv` library used; no hardcoded values |

---

## 🚀 Framework Highlights

- 📄 **Page Object Model** for clean, maintainable code.
- 🔐 **.env configuration** to store secrets securely.
- ⚡ **Parallel test execution** using `pytest-xdist`.
- 🔁 **Re-run failed tests** to reduce flakiness.
- ☁️ **LambdaTest integration** for cross-browser testing.
- 📊 **HTML reports** for clean and professional output.

---

## 📁 Project Structure

```
qa_hackathon_framework/
├── pages/
│   └── login_page.py
├── tests/
│   └── test_login.py
│   └── test_js_alerts.py
├── utils/
│   └── driver_factory.py
│   └── env_setup.py
├── reports/
├── .env
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## 🧪 How to Use

1. **Install Dependencies**
```bash
pip install -r requirements.txt
```

2. **Setup Environment Variables**  
   Inside `.env`, add:
```
LT_USERNAME=your_username
LT_ACCESS_KEY=your_access_key
RUN_REMOTE=true
USERNAME=tomsmith
PASSWORD=SuperSecretPassword!
INVALID_USERNAME=wronguser
INVALID_PASSWORD=wrongpass
```

3. **Run All Tests with Parallelism and Rerun Support**
```bash
pytest -n 2 --reruns 1 --html=reports/report.html
```

---
## 📦 Dependencies

See: [`requirements.txt`](./requirements.txt)

Includes:
- `pytest`
- `pytest-xdist`
- `pytest-html`
- `python-dotenv`
- `selenium`
