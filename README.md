# 🏦 My Safe Bank (Mini Banking System)

A mini banking management system built to practice Python Classes (OOP) and Exception Handling concepts.  
파이썬의 클래스와 **예외 처리** 개념을 학습하고 실습하기 위해 제작한 미니 은행 관리 시스템입니다.

---

## 🚀 Key Features (주요 기능)

### 1. Account Creation (계좌 개설)
- Supports both Standard Accounts and Premium Accounts (Overdraft Protection).
- 일반 계좌뿐만 아니라, 마이너스 통장(Premium) 개설 기능을 지원합니다.

### 2. Deposit & Withdrawal (입출금 시스템)
-  Implements logic to handle insufficient funds and limit checks using `raise`.
-  `raise` 키워드를 활용하여 잔액 부족 및 한도 초과 시 거래를 제한하는 로직을 구현했습니다.

### 3. Robust Exception Handling (안전한 예외 처리)
-  Prevents program crashes during user input errors or business logic failures using `try-except` blocks.
-  `try-except` 블록을 사용하여, 잘못된 입력이나 로직 오류가 발생해도 프로그램이 강제 종료되지 않고 안전하게 처리됩니다.

---

## 🛠 Tech Stack (사용 기술)

- **Language:** Python 3.x
- **Architecture:** Modular Programming with Packages (패키지 및 모듈화 구조)
- **Core Concepts:** OOP (Inheritance), Exception Handling (`try`, `except`, `raise`)

---

## 📂 Project Structure (프로젝트 구조)

```text
my_bank_project/
├── main.py                # Entry Point (실행 파일)
└── banking/               # Banking Package (핵심 로직 패키지)
    ├── __init__.py
    ├── accounts.py        # Account Classes (계좌 클래스)
    └── manager.py         # Account Manager (계좌 관리자)


```
## 📂 How to Run
Run the following command in your terminal:

```bash
python main.py
