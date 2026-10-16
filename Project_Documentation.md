# Student Performance Analytics System
## Project Documentation – Assessment Activity
**Program:** Python with AI Internship / Training  
**Organization:** EWB Courses  
**Submission Deadline:** 15 October 2026  

---

### Section 1: Project Title & Student Details
* **Project Title:** Student Performance Analytics System
* **Domain:** Python Data Analysis & Educational Informatics
* **Student Name:** [Your Full Name]
* **Student ID / Roll No:** [Your Roll Number / Student ID]
* **Email:** [Your Email Address]
* **Course:** Python with AI (EWB Courses)
* **Date of Submission:** October 2026

---

### Section 2: Objective
Educational institutions often struggle to manually consolidate, evaluate, and extract actionable insights from student academic performance and attendance records.

The primary objective of the **Student Performance Analytics System** is to automate the end-to-end evaluation of student records. The system reads structured academic data, applies vectorized numerical calculations using **NumPy**, transforms and slices records using **Pandas**, and delivers actionable analytical reports. Specific goals include:
1. Automating the calculation of total marks, average marks, and grade assignments.
2. Evaluating academic pass/fail status and attendance eligibility thresholds.
3. Generating granular subject-wise and department-wise performance metrics.
4. Identifying high achievers (top rankers) and students requiring academic support or remediation.
5. Answering practical data-driven questions regarding overall class health and curriculum difficulty.

---

### Section 3: Technologies Used
* **Programming Language:** Python 3 (v3.10+)
* **Numerical Processing Library:** **NumPy**
  * Vectorized row-wise summations (`np.sum`) and averages (`np.mean`).
  * Dispersion and positional calculations (`np.std`, `np.median`, `np.min`, `np.max`).
  * Logical array conditions (`np.round`, boolean masking).
* **Data Manipulation & Analysis Library:** **Pandas**
  * Data loading (`pd.read_csv`).
  * DataFrame creation, filtering, slicing, grouping, and aggregation.
  * Exporting structured final reports (`to_csv`).
* **Development & Version Control:** Visual Studio Code, Git & GitHub.

---

### Section 4: Dataset Description
The system utilizes a structured dataset named `students.csv` comprising 20 realistic student records across multiple departments and core subjects.

#### Important Columns:
| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `StudentID` | String | Unique identifier for each student (e.g., S101 to S120) |
| `Name` | String | Full name of the student |
| `Department` | String | Academic stream (Computer Science, AI, IT, Data Science) |
| `Math` | Float / Int | Marks scored in Mathematics (out of 100) |
| `Science` | Float / Int | Marks scored in Science (out of 100) |
| `English` | Float / Int | Marks scored in English (out of 100) |
| `ComputerScience` | Float / Int | Marks scored in Computer Science (out of 100) |
| `AI_Basics` | Float / Int | Marks scored in AI Basics (out of 100) |
| `Attendance` | Float | Percentage of classes attended by the student |

* **Total Records:** 20 Students
* **Total Features:** 9 Initial attributes + 5 Computed analytical columns

---

### Section 5: Implementation Details
The project is architected modularly into distinct components adhering to industry-standard software design:

```
Python with AI/
│── students.csv                # Raw student input dataset
│── functions.py                # Reusable analytical and computational functions
│── main.py                     # Execution engine, reporting, and CLI menu
│── students_analyzed.csv       # Exported processed results with metrics
│── Project_Documentation.md    # Formal internship documentation
│── README.md                   # GitHub repository guide
│── requirements.txt            # Python dependencies
└── .gitignore                  # Git tracking rules
```

#### Step-by-Step Processing Pipeline:
1. **Data Ingestion (`load_dataset`):**
   * Reads `students.csv` into a Pandas DataFrame with error handling for missing files or malformed rows.
   * Confirms dimensions, data types, and validates absence of null values.
2. **Numerical Computation (`calculate_student_totals_and_averages`):**
   * Converts subject marks into a NumPy 2D array (`marks_matrix`).
   * Computes row-wise sums (`np.sum(marks_matrix, axis=1)`) and averages (`np.mean(marks_matrix, axis=1)`).
3. **Grading & Pass/Fail Evaluation (`assign_grade` & `check_student_status`):**
   * Applies iterative loops across student records.
   * **Grading Criteria:**
     * $\ge 90\%$: `A+` (Outstanding)
     * $80\% - 89.99\%$: `A` (Excellent)
     * $70\% - 79.99\%$: `B` (Very Good)
     * $60\% - 69.99\%$: `C` (Good)
     * $50\% - 59.99\%$: `D` (Pass)
     * $< 50\%$: `F` (Fail)
   * **Pass/Fail Criteria:**
     * Subject passing threshold: $\ge 40$ marks in each subject.
     * Minimum attendance threshold: $\ge 75\%$.
     * Identifies academic failures, attendance shortages, and conditional passes.
4. **Statistical Analysis & Inquiries:**
   * Calculates overall class metrics (Class Average, Standard Deviation, Median).
   * Generates subject-wise summaries (Mean, High, Low, Pass Rate).
   * Generates department-wise comparison and rankings.
5. **Data Export (`export_processed_data`):**
   * Exports the augmented DataFrame with calculated fields into `students_analyzed.csv`.

---

### Section 6: Key Features
* **Modular Reusable Architecture:** Clean separation of concerns between computational logic (`functions.py`) and UI presentation (`main.py`).
* **NumPy Vectorized Calculations:** High-performance mathematical computations without manual arithmetic loops where vectorized operations excel.
* **Dual Execution Modes:**
  * **Automated Dashboard Mode:** Directly produces formatted terminal reports of all metrics.
  * **Interactive CLI Menu Mode:** (`python main.py --menu`) Allows targeted drill-downs into specific reports.
* **Subject-Level Deep Dive:** Discovers the hardest vs. easiest subjects along with standard deviation and pass rates.
* **Departmental Benchmark:** Compares student averages and passing percentages across different departments.
* **Academic Early Warning:** Automatically detects students at risk due to failing marks or attendance shortage.

---

### Section 7: Output & Execution Results

#### 1. Processed Student Records (Excerpt)
```
StudentID            Name              Department  TotalMarks  AverageMarks Grade  Attendance                 FinalStatus
     S101    Aarav Sharma        Computer Science       450.0          90.0    A+        94.5                        Pass
     S102      Diya Patel Artificial Intelligence       472.0          94.4    A+        97.0                        Pass
     S108  Sneha Kulkarni            Data Science       483.0          96.6    A+        98.5                        Pass
     S109     Aditya Nair        Computer Science       215.0          43.0     F        71.0                        Fail
     S111     Rahul Gupta  Information Technology       269.0          53.8     D        74.0 Conditional Pass (Detained)
     S115       Arjun Das  Information Technology       200.0          40.0     F        69.5                        Fail
```

#### 2. Class Summary & Statistical Metrics
* **Total Students Enrolled:** 20
* **Overall Class Average:** 75.17%
* **Highest Student Average:** 96.6% (Sneha Kulkarni - Data Science)
* **Lowest Student Average:** 40.0% (Arjun Das - Information Technology)
* **Median Class Average:** 81.4%
* **Standard Deviation:** 17.58
* **Overall Passing Rate:** 85.0% (17 passed out of 20)
* **Average Class Attendance:** 86.15%

#### 3. Subject-Wise Performance Breakdown
```
        Subject   Mean  Highest  Lowest  Median  StdDev  PassCount  PassPercentage
           Math  73.05     95.0    35.0    78.5   18.55         18            90.0
        Science  75.00     98.0    40.0    80.5   18.48         20           100.0
        English  75.40     94.0    42.0    80.0   15.26         20           100.0
ComputerScience  76.55     98.0    38.0    81.0   18.55         19            95.0
      AI_Basics  75.85     99.0    40.0    82.5   17.81         20           100.0
```

#### 4. Top 5 Ranked Students (Honor Roll)
1. **Sneha Kulkarni** (Data Science) – Average: 96.6%, Grade: A+
2. **Diya Patel** (Artificial Intelligence) – Average: 94.4%, Grade: A+
3. **Tanvi Deshmukh** (Artificial Intelligence) – Average: 93.2%, Grade: A+
4. **Kavya Menon** (Artificial Intelligence) – Average: 92.0%, Grade: A+
5. **Ananya Iyer** (Data Science) – Average: 91.8%, Grade: A+

---

### Section 8: Final Outcome
The project successfully satisfies all requirements specified in the EWB Courses guidelines:
* Completely automated raw data ingestion, transformation, and result generation.
* Replaced manual calculations with robust NumPy vector operations and Pandas methods.
* Generated clear, tabular summaries that provide instant clarity on student standing, department efficiency, and subject strengths/weaknesses.
* Successfully generated `students_analyzed.csv` for downstream reporting.

---

### Section 9: Challenges & Learning
1. **NumPy & Pandas Integration:**
   * *Challenge:* Converting heterogeneous DataFrame columns into clean NumPy matrices for fast vector calculations.
   * *Resolution:* Sliced numerical subject columns specifically with `.to_numpy(dtype=float)`, which ensured fast processing without type conflicts.
2. **Multivariate Pass/Fail and Attendance Rules:**
   * *Challenge:* Accounting for both subject-level passing criteria and institution-level attendance thresholds simultaneously.
   * *Resolution:* Designed a modular function (`check_student_status`) using programmatic loops that evaluates both academic scores and attendance thresholds, providing informative remarks.
3. **Handling Formatted CLI Outputs:**
   * *Challenge:* Ensuring terminal output remained clean, aligned, and readable across different operating systems.
   * *Resolution:* Built dynamic string banners, column width formatters, and leveraged Pandas' native string formatting.

---

### Section 10: GitHub Repository
* **Repository Name:** `student-performance-analytics`
* **Repository Link:** `https://github.com/[YOUR_GITHUB_USERNAME]/student-performance-analytics`
* **License:** MIT License
