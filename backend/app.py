from flask import Flask, jsonify

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


if __name__ == "__main__":
    app.run(debug=True)