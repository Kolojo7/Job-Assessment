const studentSelect = document.getElementById("studentSelect");
const predictBtn = document.getElementById("predictBtn");
const resultEl = document.getElementById("result");

async function loadStudentIds() {
  resultEl.textContent = "Loading students...";
  const response = await fetch("/api/students");
  if (!response.ok) {
    throw new Error("Failed to load student IDs.");
  }

  const data = await response.json();
  const ids = data.student_ids || [];
  studentSelect.innerHTML = "";

  for (const id of ids) {
    const option = document.createElement("option");
    option.value = id;
    option.textContent = id;
    studentSelect.appendChild(option);
  }

  if (ids.length > 0) {
    resultEl.textContent = "Select a student, then click predict.";
  } else {
    resultEl.textContent = "No student IDs found.";
  }
}

async function predictSelectedStudent() {
  const studentId = studentSelect.value;
  if (!studentId) {
    resultEl.textContent = "Please select a student ID.";
    return;
  }

  resultEl.textContent = "Predicting...";
  const response = await fetch("/api/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ student_id: studentId }),
  });

  const data = await response.json();
  if (!response.ok) {
    resultEl.textContent = data.error || "Prediction failed.";
    return;
  }

  resultEl.innerHTML = `
    <p><strong>Student ID:</strong> ${data.student_id}</p>
    <p><strong>Midterm Score:</strong> ${data.midterm_score}</p>
    <p><strong>Hours Studied:</strong> ${data.hours_studied}</p>
    <p><strong>Predicted Final Grade:</strong> ${data.predicted_final_grade}</p>
    <p><strong>Actual Final Grade (CSV):</strong> ${data.actual_final_grade}</p>
  `;
}

predictBtn.addEventListener("click", async () => {
  try {
    await predictSelectedStudent();
  } catch (error) {
    resultEl.textContent = error.message;
  }
});

window.addEventListener("DOMContentLoaded", async () => {
  try {
    await loadStudentIds();
  } catch (error) {
    resultEl.textContent = error.message;
  }
});
