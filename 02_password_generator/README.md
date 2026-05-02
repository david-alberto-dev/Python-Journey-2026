# 🛡️ Password Generator
A robust Python-based CLI tool designed to generate secure, randomized passwords that meet modern security standards.

## 📖 Description
The Password Generator ensures that every generated password is not just random, but also secure by design. Unlike simple random generators, this tool guarantees the inclusion of at least one lowercase letter, one uppercase letter, one digit, and one symbol.

To further enhance security, the tool uses a shuffling algorithm after assembly to ensure that the required characters don't always appear in the same initial positions.

## ⭐️ Features
- **Guaranteed Complexity:** Every password contains at least one letter, digit and symbol.
- **Length Customization:** Supports lengths from 4 to 128 characters.
- **Input Validation:** Robust error handling for non-numeric or out-of-range inputs.
- **Security Shuffle:** Uses random.shuffle() to eliminate predictable patterns in the generated string.

## 🛠️ Tech Stack
- **Language:** Python v3.14+
- **Modules:** **Random** (for logic), **string** (for data)

## 📦 Installation
1. Clone the repository:
```bash
git clone https://github.com/david-alberto-dev/Python-Journey-2026.git
```

2. Navigate to the folder:
```bash
cd Python-Journey-2026/02_password_generator/
```

## 🛠️ Usage
Run the program:
```bash
python3 password_generator.py
```

## 📄 License
This project is licensed under the **MIT License.**
