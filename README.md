
#  University Course Registration System (Python)

A modular and object‑oriented **University Course Registration System** built using Python.  
The project validates course prerequisites, manages student credit limits, loads data from CSV files, and maintains clean separation of concerns across multiple modules.

This system is ideal as a backend architecture for future GUI or web-based applications.

---

##  Features

- **Object-Oriented Architecture**
  - `Course` class to represent course information
  - `Student` class to track passed and registered courses
  - Easily extendable system design

- **Prerequisite Validation**
  - Ensures students can only register for courses after completing required prerequisites.

- **Duplicate Prevention**
  - Blocks registering a course already passed or selected.

- **Credit Limit Enforcement**
  - Students cannot exceed a total of **15 credits**.

- **CSV-Based Data Storage**
  - Course catalog stored in `courses.csv`
  - Student history stored in `history.csv`

- **Modular File Structure**
  - Clean and readable modules for scalability and maintainability.

---

##  Project Structure
course-registration-system/
│
├── course.py              # Course model
├── student.py             # Student model and validation logic
├── file_handler.py        # CSV loading utilities
├── main.py                # System orchestrator (no CLI UI needed)
├── courses.csv            # Course catalog and prerequisites
├── history.csv            # Student academic history
│
└── assets/
└── screenshots/       # Code screenshots (optional)

---

##  Data Format

### **courses.csv**
Defines all available courses:
code,title,credits,prerequisite
ADS101,Introduction to Artificial Intelligence,3,
ADS102,Programming with Python,3,
ADS201,Data Structures and Algorithms,3,ADS102
ADS202,Probability and Statistics,3,ADS103
ADS203,Database Management Systems,3,ADS102

---

### **history.csv**
Stores student course history:


student_id,course_code
250035001,ADS101
250035001,ADS102
250035001,ADS103

---

##  How the System Works

### **1️⃣ Load Data**
- `file_handler.py` reads CSV data and initializes objects.

### **2️⃣ Course Representation**
- `Course` objects store:
  - code  
  - title  
  - credits  
  - prerequisite  

### **3️⃣ Student Logic**
The `Student` class manages:
- previously passed courses  
- newly registered courses  
- total earned credits  

### **4️⃣ Validation Rules**
A course can be registered only if:

- The prerequisite is completed  
- The student has NOT previously passed it  
- The course is NOT already selected  
- Total credits do NOT exceed **15**

---

##  Technologies Used

- **Python 3**
- **Object-Oriented Programming**
- **CSV File Handling**
- **Data Structures** (lists, sets, dictionaries)
- **Modular Code Architecture**

---

##  Future Improvements

- GUI interface (Tkinter / PyQt)
- REST API implementation (Flask / FastAPI)
- Database storage (SQLite / PostgreSQL)
- Automated semester planning
- Admin dashboard and analytics

---

##  Code Screenshots

assets/screenshots/student.png
assets/screenshots/course.png
assets/screenshots/file_handler.png
assets/screenshots/main.png

---

##  License

This project is released under the **MIT License**.

---

##  Author

**MD Ratul Hasan Abid**  
Dhaka, Bangladesh  

www.linkedin.com/in/ratulabid


