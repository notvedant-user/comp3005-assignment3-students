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
