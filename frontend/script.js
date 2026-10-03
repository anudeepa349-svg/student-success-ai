// ======================================================
// STUDENT SUCCESS AI - FRONTEND JAVASCRIPT
// ======================================================

const API_URL = "http://127.0.0.1:5000";


// ======================================================
// 1. CALCULATE RISK
// ======================================================

function calculateRisk(student) {

    let risk = "Low";

    if (
        student.attendance < 60 ||
        student.internal_marks < 40 ||
        student.assignment_completion < 50 ||
        student.study_hours < 2
    ) {

        risk = "High";

    } else if (
        student.attendance < 75 ||
        student.internal_marks < 50 ||
        student.assignment_completion < 70 ||
        student.study_hours < 3
    ) {

        risk = "Medium";
    }

    return risk;
}


// ======================================================
// 2. UPDATE RISK BOX
// ======================================================

function updateRisk(risk) {

    const riskElement = document.getElementById("risk");

    const riskBox = document.querySelector(".risk");

    riskElement.textContent = risk;

    riskBox.classList.remove(
        "low",
        "medium",
        "high"
    );

    if (risk === "Low") {

        riskBox.classList.add("low");

    } else if (risk === "Medium") {

        riskBox.classList.add("medium");

    } else {

        riskBox.classList.add("high");
    }
}


// ======================================================
// 3. UPDATE PERFORMANCE
// ======================================================

function updatePerformance(student) {

    // Attendance

    document.getElementById("attendance-bar")
        .style.width =
        student.attendance + "%";

    document.getElementById("attendance-value")
        .textContent =
        student.attendance + "%";


    // Internal marks

    document.getElementById("marks-bar")
        .style.width =
        student.internal_marks + "%";

    document.getElementById("marks-value")
        .textContent =
        student.internal_marks + "%";


    // Assignment

    document.getElementById("assignment-bar")
        .style.width =
        student.assignment_completion + "%";

    document.getElementById("assignment-value")
        .textContent =
        student.assignment_completion + "%";


    // Study hours
    // Maximum represented = 10 hours

    const studyPercentage =
        Math.min(
            (student.study_hours / 10) * 100,
            100
        );

    document.getElementById("study-bar")
        .style.width =
        studyPercentage + "%";

    document.getElementById("study-value")
        .textContent =
        student.study_hours + " hours";
}


// ======================================================
// 4. UPDATE RECOMMENDATIONS
// ======================================================

function updateRecommendations(student, risk) {

    const recommendationList =
        document.getElementById("recommendation-list");

    recommendationList.innerHTML = "";


    // Attendance recommendation

    if (student.attendance < 75) {

        const li = document.createElement("li");

        li.textContent =
            "Improve attendance and attend classes regularly.";

        recommendationList.appendChild(li);
    }


    // Internal marks recommendation

    if (student.internal_marks < 50) {

        const li = document.createElement("li");

        li.textContent =
            "Focus on internal subjects and practice important topics.";

        recommendationList.appendChild(li);
    }


    // Study hours recommendation

    if (student.study_hours < 3) {

        const li = document.createElement("li");

        li.textContent =
            "Increase daily study time and follow a consistent study schedule.";

        recommendationList.appendChild(li);
    }


    // Assignment recommendation

    if (student.assignment_completion < 70) {

        const li = document.createElement("li");

        li.textContent =
            "Complete pending assignments on time.";

        recommendationList.appendChild(li);
    }


    // Low risk

    if (risk === "Low") {

        const li = document.createElement("li");

        li.textContent =
            "Good performance. Continue maintaining your current study habits.";

        recommendationList.appendChild(li);
    }


    // High risk

    if (risk === "High") {

        const li = document.createElement("li");

        li.textContent =
            "Consider seeking academic guidance from a teacher or mentor.";

        recommendationList.appendChild(li);
    }
}


// ======================================================
// 5. DISPLAY STUDENT
// ======================================================

function displayStudent(student) {

    document.getElementById("name")
        .textContent =
        student.name;

    document.getElementById("attendance")
        .textContent =
        student.attendance + "%";

    document.getElementById("marks")
        .textContent =
        student.internal_marks;

    document.getElementById("study-hours")
        .textContent =
        student.study_hours + " hours/day";

    document.getElementById("assignment")
        .textContent =
        student.assignment_completion + "%";


    // Risk

    const risk =
        student.risk_level ||
        calculateRisk(student);

    updateRisk(risk);


    // Performance

    updatePerformance(student);


    // Recommendations

    updateRecommendations(
        student,
        risk
    );


    console.log(
        "Student displayed:",
        student
    );
}


// ======================================================
// 6. LOAD DEFAULT STUDENT
// ======================================================

async function loadStudent() {

    try {

        const response =
            await fetch(
                API_URL + "/api/student"
            );


        if (!response.ok) {

            throw new Error(
                "Failed to load student data"
            );
        }


        const student =
            await response.json();


        displayStudent(student);


        console.log(
            "Default student loaded:",
            student
        );


    } catch (error) {

        console.error(
            "Error loading student:",
            error
        );

    }
}


// ======================================================
// 7. LOAD ALL STUDENTS
// ======================================================

async function loadStudents() {

    try {

        const response =
            await fetch(
                API_URL + "/api/students"
            );


        if (!response.ok) {

            throw new Error(
                "Failed to load students"
            );
        }


        const students =
            await response.json();


        const select =
            document.getElementById(
                "student-select"
            );


        // Keep first option

        select.innerHTML =
            '<option value="">Select a student</option>';


        // Add students

        students.forEach(function(student) {

            const option =
                document.createElement("option");

            option.value =
                student.id;

            option.textContent =
                student.name;

            select.appendChild(option);

        });


        console.log(
            "Students loaded:",
            students
        );


    } catch (error) {

        console.error(
            "Error loading students:",
            error
        );

    }
}


// ======================================================
// 8. LOAD SELECTED STUDENT
// ======================================================

async function loadSelectedStudent(studentId) {

    try {

        const response =
            await fetch(
                API_URL + "/api/students"
            );


        if (!response.ok) {

            throw new Error(
                "Failed to load students"
            );
        }


        const students =
            await response.json();


        const student =
            students.find(
                s => s.id == studentId
            );


        if (!student) {

            console.error(
                "Student not found"
            );

            return;
        }


        displayStudent(student);


        console.log(
            "Selected student:",
            student
        );


    } catch (error) {

        console.error(
            "Error loading selected student:",
            error
        );

    }
}


// ======================================================
// 9. ADD STUDENT
// ======================================================

document
    .getElementById("student-form")
    .addEventListener(
        "submit",
        async function(event) {

            event.preventDefault();


            const student = {

                name:
                    document
                        .getElementById(
                            "student-name"
                        )
                        .value,

                attendance:
                    Number(
                        document
                            .getElementById(
                                "student-attendance"
                            )
                            .value
                    ),

                internal_marks:
                    Number(
                        document
                            .getElementById(
                                "student-marks"
                            )
                            .value
                    ),

                study_hours:
                    Number(
                        document
                            .getElementById(
                                "student-hours"
                            )
                            .value
                    ),

                assignment_completion:
                    Number(
                        document
                            .getElementById(
                                "student-assignment"
                            )
                            .value
                    )
            };


            try {

                const response =
                    await fetch(
                        API_URL + "/api/student",
                        {

                            method: "POST",

                            headers: {
                                "Content-Type":
                                    "application/json"
                            },

                            body:
                                JSON.stringify(
                                    student
                                )
                        }
                    );


                if (!response.ok) {

                    throw new Error(
                        "Failed to add student"
                    );
                }


                const result =
                    await response.json();


                document.getElementById(
                    "form-message"
                ).textContent =
                    result.message ||
                    "Student added successfully";


                console.log(
                    "Student added:",
                    result
                );


                // Clear form

                document
                    .getElementById(
                        "student-form"
                    )
                    .reset();


                // Refresh student list

                await loadStudents();


                // Refresh dashboard

                await loadStudent();


            } catch (error) {

                console.error(
                    "Error adding student:",
                    error
                );


                document.getElementById(
                    "form-message"
                ).textContent =
                    "Failed to add student.";

            }

        }
    );


// ======================================================
// 10. STUDENT SELECTION
// ======================================================

document
    .getElementById("student-select")
    .addEventListener(
        "change",
        function() {

            const studentId =
                this.value;


            if (studentId) {

                loadSelectedStudent(
                    studentId
                );

            }

        }
    );


// ======================================================
// 11. START APPLICATION
// ======================================================

window.addEventListener(
    "load",
    function() {

        loadStudent();

        loadStudents();

    }
);