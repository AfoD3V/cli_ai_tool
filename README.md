# CLI AI Tool

A simple command-line interface for chatting with a Large Language Model (LLM) via the DeepInfra API.

## Table of Contents

- [Description](#description)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)

---

## Description

This application allows you to interact with an LLM directly from your terminal. It supports Markdown-formatted responses and maintains conversation history within a session.

## Requirements

- Python 3.11 or newer
- DeepInfra account and API key
- [uv](https://github.com/astral-sh/uv) (fast Python package installer)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd cli_ai_tool
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies using [uv](https://github.com/astral-sh/uv):
   ```bash
   uv pip install -r requirements.txt
   ```
   Or, if you use `pyproject.toml`:
   ```bash
   uv pip install -r requirements.txt
   ```

## Configuration

Create a `.env` file in the project root and add your API key:
```
API_KEY=your_api_key
```

## Usage

To start the application:
```bash
python main.py
```

or

```bash
uv run main.py
```

- Type your message and press Enter.
- The model's response will be displayed in the terminal with Markdown formatting.
- To exit, type `exit`.

### Example

```
Prompt: How does Python work?
```

## Project Structure

- `main.py` – main application file (bot and CLI logic)
- `.env` – API key file (do not commit to version control)
- `requirements.txt` or `pyproject.toml` – project dependencies

## License

This project is intended for learning and experimentation.

---