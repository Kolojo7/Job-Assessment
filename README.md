# Student Final Grade Predictor

## What This Is
This is a simple full-stack app that predicts a student's final grade using:
- `Midterm_Score`
- `Hours_Studied` (after midterm)

Frontend lets you select a `Student_ID`, then calls the backend to return the predicted final grade.

## Requirements
- Python 3.10+

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

## How To Use
1. Open the app in your browser.
2. Select a `Student_ID`.
3. Click **Predict Final Grade**.
4. View the prediction result.

## Model And Data
- Dataset: `backend/student_performance.csv`
- Trained model: `backend/final_grade_model.pkl`
- Training notebook: `notebooks/Task1.ipynb`
- `notebooks/Task1.ipynb` is the exact training source used to produce `backend/final_grade_model.pkl`.
