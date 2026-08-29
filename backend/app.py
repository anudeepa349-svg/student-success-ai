from flask import Flask, jsonify, request

app = Flask(__name__)


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
def add_student():
    data = request.get_json()

    return jsonify({
        "message": "Student data received successfully",
        "student": data
    })


if __name__ == "__main__":
    app.run(debug=True)