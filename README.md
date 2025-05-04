
# 🧠 CLI AI Tool

A simple command-line interface for chatting with a Large Language Model (LLM) using the DeepInfra API.

---

## 📖 Table of Contents

- [Overview](#overview)  
- [Requirements](#requirements)  
- [Installation](#installation)  
- [Configuration](#configuration)  
- [Usage](#usage)  
- [Project Structure](#project-structure)  
- [License](#license)  

---

## 📌 Overview

This tool allows you to chat with a powerful LLM directly from your terminal. It supports:

- Markdown rendering for clean output
- Session-based message history
- Lightweight setup using `uv`

---

## ⚙️ Requirements

- Python **3.11+**
- [DeepInfra](https://deepinfra.com/) account and API key
- [`uv`](https://github.com/astral-sh/uv) for dependency management (alternative to pip)

---

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd cli_ai_tool
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. **Install dependencies using `uv`**
   - If you're using `requirements.txt`:
     ```bash
     uv pip install -r requirements.txt
     ```
   - Or if using `pyproject.toml`:
     ```bash
     uv pip install
     ```

---

## 🔘 Configuration

Create a `.env` file in the project root with your API key:

```env
API_KEY=your_deepinfra_api_key
```

> ✅ Tip: Never commit `.env` files to version control.

---

## 💡 Usage

Run the chatbot with:

```bash
uv run main.py
```

Alternatively (if not using `uv run`):

```bash
python main.py
```

### 🗨️ Example Interaction

```bash
Prompt: What is an LLM?
```

Terminal output:

```
LLMs (Large Language Models) are...
```

To exit the chat, type `exit`.

---

## 🗂️ Project Structure

```
cli_ai_tool/
├── main.py             # CLI logic and chatbot class
├── .env                # API key (excluded from version control)
├── requirements.txt    # Package list (if not using pyproject.toml)
└── pyproject.toml      # Optional: modern dependency management
```

---

## 📄 License

This project is intended for **learning and experimentation** purposes.  
Feel free to modify and extend it as needed.
