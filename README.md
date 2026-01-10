# Takeover Experiment Platform

A web-based experimentation platform for studying strategic decision-making under asymmetric information.  
Built with **Python (oTree/Django)** and **HTML/CSS**, the app implements randomized treatments, role-based user flows, payoff computation, and clean data export for downstream analysis.

This project demonstrates how to design, deploy, and maintain an interactive experiment / web app with reliable data pipelines and reproducible logic.

---

## Key Features

- **Randomized assignment** of participants to roles and treatments
- **Multi-round sessions** with role-based permissions
- **Server-side input validation** to prevent invalid or inconsistent actions
- **Deterministic payoff computation** from user decisions
- **Export-ready datasets** designed for analysis in Python / SQL / R
- **Reproducible configuration** using centralized constants and settings

---

## Tech Stack

- **Backend:** Python, oTree (Django-based)
- **Frontend:** HTML, CSS, JavaScript (oTree templates)
- **Data:** CSV exports (analysis-ready schema)
- **Tooling:** Git, virtual environments

---

## Project Structure

```text
experiment_takeover/
├── app_takeover/            # Core experiment logic (models, pages, payoff rules)
│   ├── __init__.py
│   ├── models.py            # Game state, roles, payoff logic
│   ├── pages.py             # Participant flow and UI routing
│   ├── templates/           # HTML templates
│   └── tests.py             # (Optional) logic tests
├── settings.py              # Global experiment configuration
├── requirements.txt         # Python dependencies
├── README.md
└── examples/
    └── sample_output.csv    # Example anonymized data export



---

## How It Works

1. Participants join a session and are **randomly assigned** to a role.
2. Treatments are assigned at the session or group level.
3. Participants make decisions subject to **input constraints**.
4. The server computes payoffs deterministically from decisions.
5. Results are stored and exported as structured datasets.

This architecture mirrors real-world **A/B testing**, **market simulation**, and **behavioral data collection** systems.

---

## Quickstart (Local)

```bash
# 1. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the local server
otree devserver

