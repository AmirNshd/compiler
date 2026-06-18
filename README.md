# 🧠 Compiler Construction Project (Tokenizer-Based Interpreter)

**Course:** Design and Analysis of Algorithms / Compiler Fundamentals (not specified in code)

**Status:** Complete

**Instructor:** Dr. Arash Deldari


---

## 📂 Project Overview

| Project                          | Concept          | Description                                                                                                                 |
| -------------------------------- | ---------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **1. Custom Compiler Tokenizer** | Lexical Analysis | A rule-based tokenizer that converts source code into structured tokens while handling errors and partial parsing recovery. |

---

## 1️⃣ Custom Compiler Tokenizer

**Location:** `/compiler-main`

This project implements the lexical analysis phase of a compiler. It reads source code from a text file, removes whitespace, and converts the input into a stream of tokens using deterministic matching rules and regex-style scanning logic. It supports identifiers, numeric literals, string literals, operators, keywords, and delimiters.

The system also includes error handling via custom exceptions and continues processing after encountering invalid input.

### Key Components

* **Token System:** Defines a `Token` class with type, value, and positional indices (start/end).
* **Token Types:** Supports identifiers, keywords, operators, delimiters, numbers, and literals via an enum-based type system.
* **Keyword & Operator Table:** Predefined token dictionary for reserved words and multi-character operators (e.g., `<=`, `>=`, `==`).
* **Tokenizer Engine:** Scans input sequentially and applies rule-based matching for each token type.
* **Number Parsing Logic:** Supports integers, floating-point numbers, and scientific notation (e.g., `1.2e-5`).
* **String Literal Parsing:** Handles quoted strings with escape character awareness.
* **Identifier Rules:** Enforces a custom rule where identifiers must start with an uppercase letter.
* **Error Handling:** Uses `InvalidToken` exceptions to report lexical errors while continuing parsing when possible.

---

## ⚙️ Language Specification (Supported Tokens)

* **Identifiers:** Must start with an uppercase letter and may contain alphanumeric characters.
* **Numbers:** Integers, decimals, and scientific notation.
* **Literals:** Double-quoted strings with escape support.
* **Operators:** `+ - * / ^ Div inc dec`, comparison operators (`< <= > >= == <>`)
* **Keywords:** `if`, `while`, `until`, `repeat`, `for`
* **Delimiters:** `[ ] ( ) { } ;`

---

## 💻 How to Run

```bash
python main.py
```

Run the command inside the `compiler-main` directory.

### Input File

The program reads input from:

```
text.txt
```

Each line is tokenized independently, whitespace is ignored, and results are printed per line.

---

## ⚠️ Error Handling Behavior

When invalid tokens are detected:

* A custom exception `InvalidToken` is raised.
* The tokenizer skips problematic characters.
* Partial tokens before the error are still preserved.
* Processing continues for remaining input (fault-tolerant lexical analysis).

---

## 🛠 Tech Stack

* **Language:** Python 3.x
* **Core Concepts:**

  * Compiler Design (Lexical Analysis)
  * Finite State Scanning Logic
  * Regular Expression Concepts (implicit)
  * Error Recovery Strategies
* **Libraries:** Standard Python only

---

## 📚 Topics Covered

* Tokenization / Lexical Analysis
* Compiler Front-End Design
* Finite-State Parsing Logic
* Error Detection and Recovery
* Rule-Based Language Design
* Symbol Tables (basic keyword/operator mapping)

---

## 📅 Date

**February 2025**

---
