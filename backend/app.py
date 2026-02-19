from pathlib import Path

import joblib
import pandas as pd
from flask import Flask, jsonify, request


BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR.parent / "frontend"
CSV_PATH = BASE_DIR / "student_performance.csv"
MODEL_PATH = BASE_DIR / "final_grade_model.pkl"

app = Flask(__name__, static_folder=str(FRONTEND_DIR), static_url_path="")


def load_assets():
    students_df = pd.read_csv(CSV_PATH, dtype={"Student_ID": str})
    students_df["Student_ID"] = students_df["Student_ID"].str.strip().str.zfill(4)

    model_bundle = joblib.load(MODEL_PATH)
    if isinstance(model_bundle, dict):
        model = model_bundle["model"]
        features = model_bundle.get("features", ["Midterm_Score", "Hours_Studied"])
    else:
        model = model_bundle
        features = ["Midterm_Score", "Hours_Studied"]

    return students_df, model, features


STUDENTS_DF, MODEL, FEATURE_COLUMNS = load_assets()


@app.get("/api/health")
def health_check():
    return jsonify({"status": "ok"})


@app.get("/api/students")
def get_students():
    return jsonify({"student_ids": STUDENTS_DF["Student_ID"].tolist()})


@app.post("/api/predict")
def predict_final_grade():
    payload = request.get_json(silent=True) or {}
    raw_student_id = payload.get("student_id")
    if raw_student_id is None:
        return jsonify({"error": "student_id is required"}), 400

    student_id = str(raw_student_id).strip().zfill(4)
    student_row = STUDENTS_DF.loc[STUDENTS_DF["Student_ID"] == student_id]
    if student_row.empty:
        return jsonify({"error": f"student_id '{student_id}' not found"}), 404

    student = student_row.iloc[0]
    feature_values = {name: float(student[name]) for name in FEATURE_COLUMNS}
    features_df = pd.DataFrame([feature_values])

    predicted_grade = float(MODEL.predict(features_df)[0])
    response = {
        "student_id": student_id,
        "midterm_score": float(student["Midterm_Score"]),
        "hours_studied": float(student["Hours_Studied"]),
        "predicted_final_grade": round(predicted_grade, 2),
        "actual_final_grade": float(student["Final_Grade"]),
    }
    return jsonify(response)


@app.get("/")
def serve_index():
    return app.send_static_file("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
