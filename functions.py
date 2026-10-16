"""
functions.py
Reusable helper functions for Student Performance Analytics System.
Technologies used: Python, NumPy, Pandas.
"""

import numpy as np
import pandas as pd


def load_dataset(file_path: str) -> pd.DataFrame:
    """
    Loads student dataset from a CSV file into a Pandas DataFrame.
    Validates data presence and returns the DataFrame.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"[INFO] Successfully loaded dataset: '{file_path}'")
        print(f"[INFO] Total Records: {len(df)} | Total Columns: {len(df.columns)}")
        return df
    except FileNotFoundError:
        print(f"[ERROR] File not found at: {file_path}")
        raise
    except Exception as e:
        print(f"[ERROR] An error occurred while loading data: {e}")
        raise


def get_subject_columns() -> list:
    """
    Returns the list of subject column names in the dataset.
    """
    return ["Math", "Science", "English", "ComputerScience", "AI_Basics"]


def calculate_student_totals_and_averages(df: pd.DataFrame, subject_cols: list) -> pd.DataFrame:
    """
    Calculates total marks and average marks for each student using NumPy operations.
    Adds 'TotalMarks' and 'AverageMarks' columns to the DataFrame.
    """
    # Extract marks matrix as a NumPy 2D array
    marks_matrix = df[subject_cols].to_numpy(dtype=float)

    # Use NumPy for row-wise sum and mean calculations
    totals = np.sum(marks_matrix, axis=1)
    averages = np.mean(marks_matrix, axis=1)

    # Assign back to DataFrame with rounded values
    df["TotalMarks"] = totals
    df["AverageMarks"] = np.round(averages, 2)
    return df


def assign_grade(average_mark: float) -> str:
    """
    Assigns letter grade according to clearly defined grading rule:
    - 90 to 100: A+ (Outstanding)
    - 80 to 89.99: A (Excellent)
    - 70 to 79.99: B (Very Good)
    - 60 to 69.99: C (Good)
    - 50 to 59.99: D (Pass)
    - Below 50: F (Fail)
    """
    if average_mark >= 90:
        return "A+"
    elif average_mark >= 80:
        return "A"
    elif average_mark >= 70:
        return "B"
    elif average_mark >= 60:
        return "C"
    elif average_mark >= 50:
        return "D"
    else:
        return "F"


def check_student_status(row: pd.Series, subject_cols: list, passing_mark: float = 40.0, min_attendance: float = 75.0) -> dict:
    """
    Checks pass/fail status and attendance eligibility using loops and conditional logic.
    A student passes academically if marks in every subject >= passing_mark.
    Attendance requirement is >= min_attendance %.
    """
    academic_pass = True
    failed_subjects = []

    # Using loop to check each individual subject score
    for subject in subject_cols:
        score = row[subject]
        if score < passing_mark:
            academic_pass = False
            failed_subjects.append(subject)

    attendance_ok = row["Attendance"] >= min_attendance

    # Overall determination
    if academic_pass and attendance_ok:
        status = "Pass"
        remarks = "Cleared with good attendance"
    elif not academic_pass and not attendance_ok:
        status = "Fail"
        remarks = f"Failed in: {', '.join(failed_subjects)}; Attendance Shortage ({row['Attendance']}%)"
    elif not academic_pass:
        status = "Fail"
        remarks = f"Failed in: {', '.join(failed_subjects)}"
    else:
        status = "Conditional Pass (Detained)"
        remarks = f"Academic pass but Attendance Shortage ({row['Attendance']}%)"

    return {
        "AcademicPass": academic_pass,
        "AttendanceStatus": "Eligible" if attendance_ok else "Shortage",
        "FinalStatus": status,
        "Remarks": remarks
    }


def process_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Applies metrics calculation, grading, and status determination across all students.
    Demonstrates usage of loops, functions, and NumPy.
    """
    subject_cols = get_subject_columns()
    df = calculate_student_totals_and_averages(df, subject_cols)

    # Use loops and functions to compute grades and status
    grades = []
    academic_flags = []
    attendance_flags = []
    final_statuses = []
    remarks_list = []

    # Iterating over each student row using loop
    for idx, row in df.iterrows():
        grade = assign_grade(row["AverageMarks"])
        status_info = check_student_status(row, subject_cols)

        grades.append(grade)
        academic_flags.append(status_info["AcademicPass"])
        attendance_flags.append(status_info["AttendanceStatus"])
        final_statuses.append(status_info["FinalStatus"])
        remarks_list.append(status_info["Remarks"])

    df["Grade"] = grades
    df["AcademicPass"] = academic_flags
    df["AttendanceStatus"] = attendance_flags
    df["FinalStatus"] = final_statuses
    df["Remarks"] = remarks_list

    return df


def calculate_overall_statistics(df: pd.DataFrame) -> dict:
    """
    Computes overall class metrics using NumPy functions.
    Finds highest, lowest, and average performance.
    """
    all_averages = df["AverageMarks"].to_numpy()

    stats = {
        "TotalStudents": len(df),
        "ClassAverage": float(np.round(np.mean(all_averages), 2)),
        "HighestAverage": float(np.round(np.max(all_averages), 2)),
        "LowestAverage": float(np.round(np.min(all_averages), 2)),
        "MedianAverage": float(np.round(np.median(all_averages), 2)),
        "StdDeviation": float(np.round(np.std(all_averages), 2)),
        "TotalPassCount": int(np.sum(df["FinalStatus"] == "Pass")),
        "TotalFailCount": int(np.sum(df["FinalStatus"].str.startswith("Fail"))),
        "ConditionalCount": int(np.sum(df["FinalStatus"].str.startswith("Conditional"))),
        "AverageAttendance": float(np.round(np.mean(df["Attendance"].to_numpy()), 2))
    }
    stats["PassPercentage"] = np.round((stats["TotalPassCount"] / stats["TotalStudents"]) * 100, 2)
    return stats


def analyze_subject_wise_performance(df: pd.DataFrame, subject_cols: list) -> pd.DataFrame:
    """
    Analyzes subject-wise performance using loops and NumPy calculations:
    Mean, Max, Min, Standard Deviation, and Pass Rate.
    """
    analysis_data = []

    # Iterating through each subject using a loop
    for subject in subject_cols:
        scores = df[subject].to_numpy(dtype=float)
        mean_score = np.round(np.mean(scores), 2)
        max_score = np.max(scores)
        min_score = np.min(scores)
        median_score = np.round(np.median(scores), 2)
        std_score = np.round(np.std(scores), 2)
        passed_students = np.sum(scores >= 40.0)
        pass_rate = np.round((passed_students / len(scores)) * 100, 2)

        analysis_data.append({
            "Subject": subject,
            "Mean": mean_score,
            "Highest": max_score,
            "Lowest": min_score,
            "Median": median_score,
            "StdDev": std_score,
            "PassCount": int(passed_students),
            "PassPercentage": pass_rate
        })

    return pd.DataFrame(analysis_data)


def get_top_performers(df: pd.DataFrame, top_n: int = 5) -> pd.DataFrame:
    """
    Identifies top-performing students based on average marks.
    """
    sorted_df = df.sort_values(by="AverageMarks", ascending=False).reset_index(drop=True)
    top_students = sorted_df.head(top_n).copy()
    top_students["Rank"] = range(1, len(top_students) + 1)
    return top_students[["Rank", "StudentID", "Name", "Department", "TotalMarks", "AverageMarks", "Grade", "Attendance"]]


def get_lowest_performers(df: pd.DataFrame, bottom_n: int = 3) -> pd.DataFrame:
    """
    Identifies lowest performing students needing academic intervention.
    """
    sorted_df = df.sort_values(by="AverageMarks", ascending=True).reset_index(drop=True)
    low_students = sorted_df.head(bottom_n).copy()
    return low_students[["StudentID", "Name", "Department", "TotalMarks", "AverageMarks", "Grade", "FinalStatus", "Attendance"]]


def analyze_department_performance(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generates department-wise comparison for students.
    """
    dept_summary = []
    departments = df["Department"].unique()

    # Loop through each department
    for dept in departments:
        dept_subset = df[df["Department"] == dept]
        dept_averages = dept_subset["AverageMarks"].to_numpy()
        pass_count = np.sum(dept_subset["FinalStatus"] == "Pass")

        dept_summary.append({
            "Department": dept,
            "StudentCount": len(dept_subset),
            "DepartmentAverage": np.round(np.mean(dept_averages), 2),
            "HighestAverage": np.max(dept_averages),
            "LowestAverage": np.min(dept_averages),
            "PassRate(%)": np.round((pass_count / len(dept_subset)) * 100, 2)
        })

    return pd.DataFrame(dept_summary).sort_values(by="DepartmentAverage", ascending=False).reset_index(drop=True)


def get_grade_distribution(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates frequency and percentage for each letter grade.
    """
    grade_order = ["A+", "A", "B", "C", "D", "F"]
    grade_counts = df["Grade"].value_counts().to_dict()

    dist = []
    for g in grade_order:
        count = grade_counts.get(g, 0)
        percentage = np.round((count / len(df)) * 100, 2)
        dist.append({"Grade": g, "StudentCount": count, "Percentage(%)": percentage})

    return pd.DataFrame(dist)


def export_processed_data(df: pd.DataFrame, output_path: str = "students_analyzed.csv") -> None:
    """
    Exports processed DataFrame to a CSV file.
    """
    df.to_csv(output_path, index=False)
    print(f"[SUCCESS] Processed data saved successfully to '{output_path}'")
