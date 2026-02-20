# Student Final Grade Predictor

## What This Is
This is a simple full-stack app that predicts a student's final grade using:
- `Midterm_Score`
- `Hours_Studied` (after midterm)

Frontend lets you select a `Student_ID`, then calls the backend to return the predicted final grade.

## Requirements
- Python 3.10+
- Docker (optional, for container build/run)

## Run The Project (Windows)
From the project root:

```powershell
.\setup.bat
.\start.bat
```

Open:
- `http://127.0.0.1:5000`

Stop server:
- `Ctrl + C`

## Manual Start (Any OS)
Create and activate a virtual environment, then run the app.

Create venv:
```bash
python -m venv .venv
```

Activate venv:

Windows (PowerShell):
```powershell
.\.venv\Scripts\Activate.ps1
```

Windows (Command Prompt):
```bat
.\.venv\Scripts\activate.bat
```

macOS/Linux:
```bash
source .venv/bin/activate
```

Install dependencies and start:
```bash
pip install -r backend/requirements.txt
python backend/app.py
```

## Backend Tests And Lint (Local)
These are the same checks used by the CI pipeline.

```bash
cd backend
pytest test_api.py
flake8
```

## Docker (Local)
Build image:
```bash
docker build -t job-assessment:dev .
```

Run container:
```bash
docker run --rm -p 5000:5000 job-assessment:dev
```

Health check:
```bash
curl http://127.0.0.1:5000/api/health
```

## How To Run The Pipeline
1. Push commits to a branch and open a PR into `main` to run checks.
2. Push to `main` to run checks and build/push the Docker image.
3. Optional: run manually from the GitHub `Actions` tab using `workflow_dispatch`.

## How To Verify Docker Push
After a successful `main` pipeline:

```bash
docker pull kolojo7/job_assessment:latest
docker run --rm -p 5000:5000 kolojo7/job_assessment:latest
```

Then open:
- `http://127.0.0.1:5000`

## Model And Data
- Dataset: `backend/student_performance.csv`
- Trained model: `backend/final_grade_model.pkl`
- Training notebook: `notebooks/Task1.ipynb`
- `notebooks/Task1.ipynb` is the exact training source used to produce `backend/final_grade_model.pkl`.
