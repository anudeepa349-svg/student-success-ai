from flask import Flask, jsonify, request
from flask_cors import CORS

from database import (
    create_table,
    add_student,
    get_student,
    get_all_students
)

import joblib
import pandas as pd
import os


# =====================================================
# FLASK APPLICATION
# =====================================================

app = Flask(__name__)

CORS(app)


# =====================================================
# DATABASE
# =====================================================

create_table()


# =====================================================
# LOAD MACHINE LEARNING MODEL
# =====================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "ml",
    "risk_model.pkl"
)


try:

    model = joblib.load(MODEL_PATH)

    print("Machine Learning model loaded successfully!")

except Exception as error:

    model = None

    print("Error loading Machine Learning model:")
    print(error)


# =====================================================
# ML RISK PREDICTION
# =====================================================

def predict_risk(student):

    if model is None:

        return "Unknown"


    input_data = pd.DataFrame([
        {
            "attendance": student["attendance"],
            "internal_marks": student["internal_marks"],
            "study_hours": student["study_hours"],
            "assignment_completion":
                student["assignment_completion"]
        }
    ])


    prediction = model.predict(input_data)

    return prediction[0]


# =====================================================
# RECOMMENDATIONS
# =====================================================

def generate_recommendations(student):

    recommendations = []


    if student["attendance"] < 75:

        recommendations.append(
            "Improve attendance and attend classes regularly."
        )


    if student["internal_marks"] < 50:

        recommendations.append(
            "Focus more on internal exam preparation."
        )


    if student["study_hours"] < 2:

        recommendations.append(
            "Increase daily study time to at least 2 hours."
        )


    if student["assignment_completion"] < 60:

        recommendations.append(
            "Complete pending assignments on time."
        )


    if not recommendations:

        recommendations.append(
            "Great performance! Keep maintaining your current study routine."
        )


    return recommendations


# =====================================================
# HOME
# =====================================================

@app.route("/")
def home():

    return jsonify({
        "message":
            "Student Success AI Backend is running!"
    })


# =====================================================
# HEALTH CHECK
# =====================================================

@app.route("/api/health")
def health():

    return jsonify({
        "status": "success",
        "message": "Backend is healthy"
    })


# =====================================================
# GET LATEST STUDENT
# =====================================================

@app.route("/api/student", methods=["GET"])
def student():

    student_data = get_student()


    if student_data:

        # ML prediction

        student_data["risk_level"] = predict_risk(
            student_data
        )


        # Recommendations

        student_data["recommendations"] = (
            generate_recommendations(
                student_data
            )
        )


        return jsonify(student_data)


    return jsonify({
        "message": "No student found"
    }), 404


# =====================================================
# ADD STUDENT
# =====================================================

@app.route("/api/student", methods=["POST"])
def add_student_api():

    data = request.get_json()


    if not data:

        return jsonify({
            "error":
                "No student data received"
        }), 400


    required_fields = [
        "name",
        "attendance",
        "internal_marks",
        "study_hours",
        "assignment_completion"
    ]


    for field in required_fields:

        if field not in data:

            return jsonify({
                "error":
                    f"Missing field: {field}"
            }), 400


    # Save student to database

    add_student(
        data["name"],
        data["attendance"],
        data["internal_marks"],
        data["study_hours"],
        data["assignment_completion"]
    )


    return jsonify({

        "message":
            "Student added successfully",

        "student":
            data

    }), 201


# =====================================================
# GET ALL STUDENTS
# =====================================================

@app.route("/api/students", methods=["GET"])
def students():

    student_list = get_all_students()


    for student in student_list:

        # ML prediction

        student["risk_level"] = predict_risk(
            student
        )


        # Recommendations

        student["recommendations"] = (
            generate_recommendations(
                student
            )
        )


    return jsonify(student_list)


# =====================================================
# RUN APPLICATION
# =====================================================

if __name__ == "__main__":

    app.run(
        debug=True
    )