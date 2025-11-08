# comp3005-assignment3-students
COMP 3005 – Assignment 3 – PostgreSQL CRUD Application

# COMP 3005 – Assignment 3 – PostgreSQL CRUD (Students)

## Overview
Small Python app that connects to a PostgreSQL database and performs CRUD on a `students` table.

## Tech
- PostgreSQL 17 + pgAdmin 4
- Python 3.x, `psycopg2-binary`, `python-dotenv`

## Repo Structure
comp3005-assignment3-students/
│
├── db/
│   ├── schema.sql          # the CREATE TABLE command
│   └── seed.sql            # the INSERT commands
│
├── app/
│   └── main.py             # (or main.java, app.js etc. depending on your language)
│
├── README.md               # you’ll fill this later
└── docs/
    └── screenshots/ 


## Prerequisites
- PostgreSQL installed and running on localhost:5432
- A database named `students_db`
- pgAdmin 4 (optional for verification)

## Setup (Database)
1. Open pgAdmin → connect to server.
2. Create DB `students_db` (if not created).
3. Query Tool on `students_db` → run `db/schema.sql`.
4. Run `db/seed.sql`.
5. Verify: `SELECT * FROM students;` → should show 3 rows.

## Setup (App)
```bash
# clone repo
git clone https://github.com/<your-username>/comp3005-assignment3-students.git
cd comp3005-assignment3-students

# venv
python -m venv .venv
# Windows:
.\.venv\Scripts\activate
# macOS/Linux:
# source .venv/bin/activate

# install deps
pip install psycopg2-binary python-dotenv

Step 1 — Read (GET) :-
1. Shows all current students.
2. Make sure only getAllStudents() is uncommented, and all other lines are commented.
3. Run : python app/main.py
4. You’ll see the initial 3 rows (John, Jane, Jim).
5. In pgAdmin, open students → View/Edit Data → All Rows to confirm.

Step 2 — Create (INSERT)
1. Adds a new student record.
2. Comment out getAllStudents().
3. Uncomment the addStudent() line only.
4. Run : python app/main.py
5. The console prints something like Inserted student_id=5.
6. In pgAdmin, click the Reload (circular arrow) button in the    data grid → you should now see the new student (Alice).

Step 3 — Update (UPDATE)
1. Updates the student’s email address.
2. While uncommenting this step, make sure to keep Step 2 commented — otherwise you’ll try to insert Alice again and cause a duplicate email error.
3. Comment out addStudent().
4. Uncomment only: updateStudentEmail(5, "alice.w@example.com")
(Replace 5 with the correct ID shown in your INSERT output if it’s different.)
5. Run : python app/main.py
6. The console prints Updated email for student_id=5.
7. Reload the pgAdmin data grid → email should now show alice.w@example.com.

Step 4 — Delete (DELETE)
1. Deletes the student record you just added/updated.
2. Comment out the updateStudentEmail() line.
3. Uncomment : deleteStudent(5)
(Use the same student ID.)
4. Run : python app/main.py
5. The console prints Deleted student_id=5.
6. Reload pgAdmin → you should now see only 3 rows again (John, Jane, Jim).


Expected Console Output Summary
== All Students ==
  1 | John Doe | john.doe@example.com | 2023-09-01
  2 | Jane Smith | jane.smith@example.com | 2023-09-01
  3 | Jim Beam | jim.beam@example.com | 2023-09-02
Inserted student_id=5
Updated email for student_id=5 -> alice.w@example.com
Deleted student_id=5