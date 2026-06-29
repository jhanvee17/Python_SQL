# 🎓 Student Result Management System

A command-line based **Student Result Management System** developed using **Python** and **MySQL**. This project allows users to manage student records, enter marks, generate results, display individual results, and view the topper list.

---

## 🚀 Features

- ➕ Add new student records
- 📝 Enter marks for five subjects
- 📊 Automatically calculate:
  - Total Marks
  - Percentage
  - Grade
- 📄 Display individual student results
- 🏆 View Top N toppers
- 💾 Stores all data in a MySQL database

---

## 🛠️ Tech Stack

- Python
- MySQL
- mysql-connector-python

---

## 📂 Database Structure

The project uses the following tables:

### Student
| Column | Description |
|---------|-------------|
| std_id | Student ID |
| name | Student Name |
| class | Student Class |
| roll_no | Roll Number |
| city | City |

### Subject
| Column | Description |
|---------|-------------|
| subject_id | Subject ID |
| subject_name | Subject Name |

### Marks
| Column | Description |
|---------|-------------|
| std_id | Student ID |
| subject_id | Subject ID |
| marks | Marks Obtained |

### Result
| Column | Description |
|---------|-------------|
| std_id | Student ID |
| total | Total Marks |
| percentage | Percentage |
| grade | Grade |

---

## 📋 Menu

```
1. Add Student
2. Enter Marks
3. Generate Result
4. Show Result
5. Topper List
6. Exit
```

---

## 🎯 Grading Criteria

| Percentage | Grade |
|------------|-------|
| 85 and above | A |
| 75 – 84 | B |
| 60 – 74 | C |
| 45 – 59 | D |
| 33 – 44 | E |
| Below 33 | F |

---

## ▶️ How to Run

1. Clone the repository

```bash
git clone https://github.com/jhanvee17/Python_SQL.git
```

2. Navigate to the project folder

```bash
cd Python_SQL
```

3. Install the required package

```bash
pip install mysql-connector-python
```

4. Create the MySQL database and required tables.

5. Update the database credentials in `python.py`

```python
host="localhost"
user="root"
password="your_password"
database="result_project"
```

6. Run the project

```bash
python python.py
```

---

## 📸 Sample Output

```
1 Add Student
2 Enter Marks
3 Generate Result
4 Show Results
5 Topper List
6 Exit
Enter your choice:
```

---

## 📚 Concepts Used

- Python Functions
- Loops
- Match-Case Statement
- SQL CRUD Operations
- Joins
- Aggregate Functions
- Conditional Statements
- Database Connectivity using mysql.connector

---

## 👩‍💻 Author

**Jhanvee Solanki**

GitHub: https://github.com/jhanvee17

---

## 📄 License

This project is created for learning and educational purposes.