# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python CLI chatbot application that interfaces with the DeepInfra API to provide terminal-based AI conversations. The application uses `uv` for dependency management and consists of two main classes:

- `ChatBot` - handles API communication with DeepInfra's LLM services
- `CLI` - provides the terminal interface with rich formatting

## Development Commands

### Running the Application
```bash
uv run main.py
```

### Dependency Management
```bash
# Install dependencies
uv pip install

# Add new dependency
uv add <package-name>
```

### Environment Setup
Create a `.env` file with:
```
API_KEY=your_deepinfra_api_key
```

## Architecture

### Core Components

**ChatBot Class (`main.py:15-114`)**
- Manages conversation state via `self.messages` list
- Handles DeepInfra API communication through `ask()` method
- Supports configurable models and system instructions
- Uses `@yaspin` decorator for loading animations

**CLI Class (`main.py:116-170`)**
- Provides terminal interface using Rich console
- Handles user input loop and markdown response rendering
- Manages application lifecycle (start/exit)

**Main Function (`main.py:172-194`)**
- Uses Typer for command-line argument parsing
- Provides interactive model selection via inquirer
- Instantiates and connects ChatBot and CLI components

### Key Dependencies
- `requests` - DeepInfra API communication
- `rich` - Terminal formatting and markdown rendering
- `typer` - CLI argument parsing
- `inquirer` - Interactive model selection
- `yaspin` - Loading spinners
- `pyfiglet` - ASCII art titles

### Test Files
- `test.py` contains Selenium-based web scraping utilities (separate from main application)

## Configuration

The application expects:
- Python 3.11+
- DeepInfra API key in `.env` file
- Model selection from predefined choices or command-line option