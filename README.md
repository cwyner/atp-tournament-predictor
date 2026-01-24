### atp-tournament-predictor

ATP tournament predictor

### Setup: Python Environment + Dependencies

If you'd like to use this project for yourself, these instructions will help you create a clean Python environment and install the required dependencies.

## Prerequisites

- **Python 3.10+** recommended (3.11 is fine)
- `pip` (Python package manager)

Verify your installation:

```bash
python3 --version
python3 -m pip --version

```

## Create a Virtual Environment

From the project root directory:

# macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

# Windows (Powershell)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install --upgrade pip
```

Confirm the environment is active:

```bash
python --version
```

## Install Dependencies

Install all required packages from `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

## Deactivate the Environment

When finished working on the project:

```bash
deactivate
```
