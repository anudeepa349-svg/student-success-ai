from flask import Flask, jsonify, request
from database import create_table, add_student

app = Flask(__name__)

create_table()


@app.route("/")
def home():
    return jsonify({
        "message": "Student Success AI Backend is running!"
    })


@app.route("/api/health")
def health():
    return jsonify({
        "status": "success",
        "message": "Backend is healthy"
    })


@app.route("/api/student")
def student():
    return jsonify({
        "name": "Demo Student",
        "attendance": 85,
        "internal_marks": 72,
        "study_hours": 3,
        "risk_level": "Low"
    })


@app.route("/api/student", methods=["POST"])
def add_student_api():
    data = request.get_json()

    name = data["name"]
    attendance = data["attendance"]
    internal_marks = data["internal_marks"]
    study_hours = data["study_hours"]
    assignment_completion = data["assignment_completion"]

    add_student(
        name,
        attendance,
        internal_marks,
        study_hours,
        assignment_completion
    )

    return jsonify({
        "message": "Student added successfully",
        "student": data
    })


if __name__ == "__main__":
    app.run(debug=True)