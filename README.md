# Student Performance Analytics System 📊🎓

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-2.x-orange.svg)](https://numpy.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.x-darkgreen.svg)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python data analytics system developed for the **Python with AI** course under **EWB Courses**. This application reads student academic data from a CSV file, performs vectorized numerical calculations and statistical modeling using **NumPy** and **Pandas**, applies grading logic, and produces comprehensive terminal reports and exported analytics files.

---

## 📌 Project Overview
The **Student Performance Analytics System** automates the computation of student totals, percentages, letter grades, pass/fail status, and attendance eligibility. In addition, it provides actionable insights such as subject-wise difficulty rankings, department-level comparisons, top performer honor rolls, and alerts for at-risk students.

### Key Objectives:
- Implement clean, reusable Python functions and loops.
- Use **NumPy** for numerical calculations (sums, means, standard deviation, percentiles).
- Use **Pandas** for structured dataset ingestion, manipulation, aggregation, and export.
- Answer real-world practical questions about student performance.

---

## 📂 Repository Structure

```text
├── students.csv             # Input dataset containing 20 student records
├── functions.py             # Reusable calculation, grading, and analysis functions
├── main.py                  # Primary entry point (Automated reporting & Interactive CLI)
├── students_analyzed.csv    # Automatically exported dataset with computed metrics
├── Project_Documentation.md # Detailed 10-section internship project documentation
├── requirements.txt         # Project dependencies (NumPy, Pandas)
├── .gitignore               # Git ignore rules for clean repository
└── README.md                # Project documentation and guide
```

---

## 🚀 Features

- **Automated Grade Assignment**: Computes overall average and assigns letter grades (`A+`, `A`, `B`, `C`, `D`, `F`) based on institutional grading rules.
- **Pass/Fail & Attendance Verification**: Evaluates whether a student cleared each subject ($\ge 40$) and satisfied the minimum mandatory attendance threshold ($\ge 75\%$).
- **Subject-Wise Deep Dive**: Evaluates average score, highest mark, lowest mark, standard deviation, and passing rates across all subjects.
- **Top Performers & Rank List**: Generates the Top 5 student honor roll.
- **Academic Early Warning System**: Flags low-performing students or those with attendance shortages for timely intervention.
- **Department Benchmarking**: Aggregates and compares performance across academic departments (AI, Data Science, CS, IT).
- **Dual Execution Modes**:
  1. **Standard Automated Mode**: Runs the complete analysis suite and prints an executive summary.
  2. **Interactive CLI Menu**: Enables users to explore individual reports on demand.
- **Data Export**: Saves all computed results directly into `students_analyzed.csv`.

---

## 🛠️ Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/student-performance-analytics.git
cd student-performance-analytics
```

### 2. Set Up a Virtual Environment (Optional but Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 💻 How to Run the Project

### Standard Automated Mode
Run the entire analytical pipeline with a single command:
```bash
python main.py
```

### Interactive CLI Menu Mode
To explore individual analysis modules interactively:
```bash
python main.py --menu
```

---

## 📊 Sample Output Preview

```text
=====================================================================================
                      STUDENT PERFORMANCE ANALYTICS SYSTEM - EWB COURSES             
=====================================================================================

-------------------------------------------------------------------------------------
                       CLASS PERFORMANCE & STATISTICAL METRICS                       
-------------------------------------------------------------------------------------
Total Students Enrolled : 20
Overall Class Average   : 75.17%
Highest Student Average : 96.6%
Lowest Student Average  : 40.0%
Median Class Average    : 81.4%
Standard Deviation      : 17.58
Pass Count              : 17 / 20 (85.0%)
Fail / Detained Count   : 3
Average Attendance      : 86.15%

-------------------------------------------------------------------------------------
                          SUBJECT-WISE PERFORMANCE BREAKDOWN                         
-------------------------------------------------------------------------------------
        Subject   Mean  Highest  Lowest  Median  StdDev  PassCount  PassPercentage
           Math  73.05     95.0    35.0    78.5   18.55         18            90.0
        Science  75.00     98.0    40.0    80.5   18.48         20           100.0
        English  75.40     94.0    42.0    80.0   15.26         20           100.0
ComputerScience  76.55     98.0    38.0    81.0   18.55         19            95.0
      AI_Basics  75.85     99.0    40.0    82.5   17.81         20           100.0

-------------------------------------------------------------------------------------
                        TOP 5 ACADEMIC PERFORMERS (HONOR ROLL)                       
-------------------------------------------------------------------------------------
 Rank StudentID           Name              Department  TotalMarks  AverageMarks Grade  Attendance
    1      S108 Sneha Kulkarni            Data Science       483.0          96.6    A+        98.5
    2      S102     Diya Patel Artificial Intelligence       472.0          94.4    A+        97.0
    3      S118 Tanvi Deshmukh Artificial Intelligence       466.0          93.2    A+        95.5
    4      S114    Kavya Menon Artificial Intelligence       460.0          92.0    A+        96.0
    5      S104    Ananya Iyer            Data Science       459.0          91.8    A+        91.5
```

---

## 🔍 Practical Assignment Questions Answered

1. **Which student has the highest average?**  
   👉 **Sneha Kulkarni (S108)** from Data Science with an average of **96.6%** (Total: 483/500, Grade: A+).

2. **Which subject has the best average?**  
   👉 **Computer Science** had the highest average at **76.55%**, while **Math** had the lowest at **73.05%**.

3. **How many students passed?**  
   👉 **17 out of 20 students (85%)** cleared all academic and attendance requirements.

4. **What is the overall class average?**  
   👉 **75.17%** with a standard deviation of **17.58**.

---

## 📋 Grading Criteria

| Average Percentage | Letter Grade | Performance Level |
| :---: | :---: | :---: |
| 90% - 100% | **A+** | Outstanding |
| 80% - 89.9% | **A** | Excellent |
| 70% - 79.9% | **B** | Very Good |
| 60% - 69.9% | **C** | Good |
| 50% - 59.9% | **D** | Pass |
| Below 50% | **F** | Fail |

*Note: In addition to marks, students must maintain a minimum of 75% attendance to avoid detention.*

---

## 👤 Author & Acknowledgments

- **Author:** [Your Name]
- **Course:** Python with AI
- **Organization:** EWB Courses
- **Submission Date:** October 2026
