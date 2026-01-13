# Behavioral Experiment Platform for Strategic Decision-Making under Asymmetric Information

This project implements a configurable experimental platform in Python (oTree) to study how information asymmetry and belief distortions affect bidding and acceptance decisions in bilateral trade.

The system supports multi-round experiments, role-based logic, incentive-compatible payoffs, and structured data output suitable for causal and structural analysis.


---
## Skills Demonstrated
- Experimental system design (multi-round, role-based logic)
- Python backend development (state management, payoff rules)
- Incentive-compatible mechanism implementation
- Data generation pipelines for behavioral analysis
- Reproducible research and clean project structure

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
├── rrrt_fri3/            # Web app: core experiment logic (models, pages, payoff rules)
│   ├── __init__.py       # Game state, roles, payoff logic, participant flow, and UI routing
│   └── templates         # HTML templates
├── settings.py           # Global experiment configuration
├── requirements.txt      # Python dependencies
├── README.md
└── examples/
    └── sample_output.csv        # Example anonymized export
```


---

## How It Works

1. Participants join a session and are randomly assigned to a role.
2. Treatments are assigned at the session or group level.
3. Participants make decisions subject to input constraints.
4. The server computes payoffs deterministically from decisions.
5. Results are stored and exported as structured datasets.

This architecture mirrors real-world A/B testing, market simulation, and behavioral data collection systems.

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

