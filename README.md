
# 🧠 CLI AI Tool

A simple command-line interface for chatting with a Large Language Model (LLM) using the DeepInfra API.

---

## 📖 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)

---

## 📌 Overview

This tool allows you to chat with a powerful LLM directly from your terminal, providing a seamless and efficient way to interact with AI.

---

## ✨ Features

- **Markdown Rendering**: Clean and readable output.
- **Session-Based History**: Keeps track of the conversation.
- **Lightweight Setup**: Uses `uv` for fast dependency management.
- **Interactive Model Selection**: Choose your preferred LLM model.

---

## ⚙️ Requirements

- Python **3.11+**
- [DeepInfra](https://deepinfra.com/) account and API key
- [`uv`](https://github.com/astral-sh/uv) for dependency management

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
   ```bash
   uv pip install
   ```

---

## 🔘 Configuration

Create a `.env` file in the project root with your API key:

```env
API_KEY=your_deepinfra_api_key
```

> ✅ **Tip**: Never commit `.env` files to version control.

---

## 💡 Usage

Run the chatbot with:

```bash
uv run main.py
```

Alternatively, if you are not using `uv run`:

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
└── pyproject.toml      # Dependency management
```

---

## 📄 License

This project is intended for **learning and experimentation** purposes. Feel free to modify and extend it as needed.
