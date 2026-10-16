"""
================================================================================
Student Performance Analytics System
--------------------------------------------------------------------------------
Course: Python with AI | EWB Courses
Technology: Python 3, NumPy, Pandas
Main Executable File: main.py
================================================================================
"""

import sys
import os
import pandas as pd
import numpy as np

# Import reusable modules from functions.py
from functions import (
    load_dataset,
    get_subject_columns,
    process_dataset,
    calculate_overall_statistics,
    analyze_subject_wise_performance,
    get_top_performers,
    get_lowest_performers,
    analyze_department_performance,
    get_grade_distribution,
    export_processed_data
)


def print_header(title: str, width: int = 85, char: str = "=") -> None:
    """Helper function to print formatted section banners."""
    print()
    print(char * width)
    print(f" {title.upper()} ".center(width, " "))
    print(char * width)


def display_dataframe_formatted(df: pd.DataFrame, title: str = None) -> None:
    """Nicely formats and prints a pandas DataFrame."""
    if title:
        print(f"\n--- {title} ---")
    print(df.to_string(index=False))


def answer_practical_questions(df: pd.DataFrame, subject_analysis: pd.DataFrame, overall_stats: dict) -> None:
    """
    Step 4: Answer key practical questions from the dataset as required by guidelines:
    - Which student has the highest average?
    - Which subject has the best average?
    - How many students passed?
    - What is the overall class average?
    """
    print_header("Step 4: Practical Analytics Questions Answered", char="*")

    # 1. Which student has the highest average?
    top_student = df.loc[df["AverageMarks"].idxmax()]
    print(f"1. Which student has the highest average?")
    print(f"   -> Top Student: {top_student['Name']} ({top_student['StudentID']})")
    print(f"   -> Department : {top_student['Department']}")
    print(f"   -> Average    : {top_student['AverageMarks']}% (Total: {top_student['TotalMarks']}/500, Grade: {top_student['Grade']})\n")

    # 2. Which subject has the best average?
    best_subject_row = subject_analysis.loc[subject_analysis["Mean"].idxmax()]
    hardest_subject_row = subject_analysis.loc[subject_analysis["Mean"].idxmin()]
    print(f"2. Which subject has the best average?")
    print(f"   -> Best Performing Subject: '{best_subject_row['Subject']}' with an average of {best_subject_row['Mean']}%")
    print(f"   -> Toughest Subject       : '{hardest_subject_row['Subject']}' with an average of {hardest_subject_row['Mean']}%\n")

    # 3. How many students passed?
    print(f"3. How many students passed?")
    print(f"   -> Fully Passed Students: {overall_stats['TotalPassCount']} out of {overall_stats['TotalStudents']} ({overall_stats['PassPercentage']}%)")
    print(f"   -> Failed / Detained    : {overall_stats['TotalFailCount'] + overall_stats['ConditionalCount']} students\n")

    # 4. What is the overall class average?
    print(f"4. What is the overall class average?")
    print(f"   -> Overall Class Average: {overall_stats['ClassAverage']}% (Std Dev: {overall_stats['StdDeviation']}, Median: {overall_stats['MedianAverage']}%)\n")


def run_full_analytics(data_path: str = "students.csv") -> None:
    """
    Executes the entire student performance analysis pipeline.
    """
    print_header("Student Performance Analytics System - EWB Courses")
    print("Initializing system and verifying prerequisites...")

    # Step 1 & 2: Load and inspect dataset
    print_header("Step 1 & 2: Dataset Loading and Initial Inspection", char="-")
    df_raw = load_dataset(data_path)
    
    print("\n[INFO] First 5 Records in Raw Dataset:")
    display_dataframe_formatted(df_raw.head())

    print("\n[INFO] Dataset Summary Info:")
    print(f"Columns: {list(df_raw.columns)}")
    print(f"Total Student Records: {len(df_raw)}")
    print(f"Missing Values: {df_raw.isnull().sum().sum()}")

    # Step 3: Process the data
    print_header("Step 3: Processing Data (Calculations, NumPy & Grading)", char="-")
    df_processed = process_dataset(df_raw.copy())
    subject_cols = get_subject_columns()

    # Display processed table
    display_cols = ["StudentID", "Name", "Department", "TotalMarks", "AverageMarks", "Grade", "Attendance", "FinalStatus"]
    print("\n[INFO] Processed Student Records Summary:")
    display_dataframe_formatted(df_processed[display_cols])

    # Step 4: Perform Statistical Analysis
    print_header("Class Performance & Statistical Metrics", char="-")
    overall_stats = calculate_overall_statistics(df_processed)
    print(f"Total Students Enrolled : {overall_stats['TotalStudents']}")
    print(f"Overall Class Average   : {overall_stats['ClassAverage']}%")
    print(f"Highest Student Average : {overall_stats['HighestAverage']}%")
    print(f"Lowest Student Average  : {overall_stats['LowestAverage']}%")
    print(f"Median Class Average    : {overall_stats['MedianAverage']}%")
    print(f"Standard Deviation      : {overall_stats['StdDeviation']}")
    print(f"Pass Count              : {overall_stats['TotalPassCount']} / {overall_stats['TotalStudents']} ({overall_stats['PassPercentage']}%)")
    print(f"Fail / Detained Count   : {overall_stats['TotalFailCount'] + overall_stats['ConditionalCount']}")
    print(f"Average Attendance      : {overall_stats['AverageAttendance']}%")

    # Subject-wise analysis
    print_header("Subject-Wise Performance Breakdown", char="-")
    subject_df = analyze_subject_wise_performance(df_processed, subject_cols)
    display_dataframe_formatted(subject_df)

    # Top Performers
    print_header("Top 5 Academic Performers (Honor Roll)", char="-")
    top_5 = get_top_performers(df_processed, top_n=5)
    display_dataframe_formatted(top_5)

    # Lowest Performers / Academic Intervention
    print_header("Students Requiring Academic Attention", char="-")
    low_performers = get_lowest_performers(df_processed, bottom_n=3)
    display_dataframe_formatted(low_performers)

    # Department-wise Analysis
    print_header("Department-Wise Performance Comparison", char="-")
    dept_df = analyze_department_performance(df_processed)
    display_dataframe_formatted(dept_df)

    # Grade Distribution
    print_header("Grade Distribution Summary", char="-")
    grade_df = get_grade_distribution(df_processed)
    display_dataframe_formatted(grade_df)

    # Answering key assignment questions
    answer_practical_questions(df_processed, subject_df, overall_stats)

    # Step 5: Export analyzed output
    print_header("Step 5: Exporting Analyzed Dataset", char="-")
    output_filename = "students_analyzed.csv"
    export_processed_data(df_processed, output_filename)

    print("\n" + "=" * 85)
    print(" [COMPLETED] Full Student Performance Analytics Executed Successfully! ".center(85, " "))
    print("=" * 85 + "\n")


def interactive_menu():
    """Interactive CLI menu to navigate different reports individually."""
    data_path = "students.csv"
    if not os.path.exists(data_path):
        print(f"[ERROR] Could not find {data_path}. Please check file location.")
        return

    df_raw = load_dataset(data_path)
    df_processed = process_dataset(df_raw.copy())
    subject_cols = get_subject_columns()

    while True:
        print("\n" + "=" * 60)
        print(" STUDENT PERFORMANCE ANALYTICS SYSTEM - MENU ")
        print("=" * 60)
        print("1. View Raw Dataset Overview")
        print("2. View Complete Processed Student Records")
        print("3. View Overall Class Statistics")
        print("4. View Subject-Wise Performance Breakdown")
        print("5. View Top 5 Ranked Students")
        print("6. View Students Requiring Support / Failed")
        print("7. View Department Performance Comparison")
        print("8. View Grade Distribution")
        print("9. Answer Practical Guidelines Questions")
        print("10. Run Full Complete Analytics Report")
        print("11. Export Processed Data to CSV")
        print("0. Exit System")
        print("-" * 60)

        choice = input("Enter your choice (0-11): ").strip()
        print()

        if choice == "1":
            print_header("Raw Dataset Preview", 60)
            display_dataframe_formatted(df_raw)
        elif choice == "2":
            print_header("Processed Records", 80)
            display_dataframe_formatted(df_processed[["StudentID", "Name", "Department", "TotalMarks", "AverageMarks", "Grade", "Attendance", "FinalStatus"]])
        elif choice == "3":
            print_header("Overall Class Statistics", 60)
            stats = calculate_overall_statistics(df_processed)
            for k, v in stats.items():
                print(f"  • {k:20}: {v}")
        elif choice == "4":
            print_header("Subject-Wise Performance", 70)
            display_dataframe_formatted(analyze_subject_wise_performance(df_processed, subject_cols))
        elif choice == "5":
            print_header("Top 5 Students", 75)
            display_dataframe_formatted(get_top_performers(df_processed, 5))
        elif choice == "6":
            print_header("Students Needing Support", 75)
            display_dataframe_formatted(get_lowest_performers(df_processed, 3))
        elif choice == "7":
            print_header("Department Performance", 70)
            display_dataframe_formatted(analyze_department_performance(df_processed))
        elif choice == "8":
            print_header("Grade Distribution", 60)
            display_dataframe_formatted(get_grade_distribution(df_processed))
        elif choice == "9":
            stats = calculate_overall_statistics(df_processed)
            subj_df = analyze_subject_wise_performance(df_processed, subject_cols)
            answer_practical_questions(df_processed, subj_df, stats)
        elif choice == "10":
            run_full_analytics(data_path)
        elif choice == "11":
            export_processed_data(df_processed, "students_analyzed.csv")
        elif choice == "0":
            print("Exiting Student Performance Analytics System. Goodbye!")
            break
        else:
            print("[WARN] Invalid option selected. Please choose between 0 and 11.")


if __name__ == "__main__":
    # If '--menu' argument is passed, launch interactive CLI, otherwise run standard automated report
    if len(sys.argv) > 1 and sys.argv[1].lower() in ["--menu", "-m", "--interactive"]:
        interactive_menu()
    else:
        run_full_analytics()
