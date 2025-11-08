import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

# -------------
# Load config
# -------------
load_dotenv()  # reads .env in project root

DB_CONFIG = {
    "host": os.getenv("PGHOST", "localhost"),
    "port": int(os.getenv("PGPORT", "5432")),
    "dbname": os.getenv("PGDATABASE", "students_db"),
    "user": os.getenv("PGUSER", "postgres"),
    "password": os.getenv("PGPASSWORD", ""),
}

def get_connection():
    """
    Open and return a new database connection using env-configured parameters.
    """
    return psycopg2.connect(
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        dbname=DB_CONFIG["dbname"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"]
    )

# -------------
# CRUD functions
# -------------

def getAllStudents():
    """
    Read: Fetch and print all students ordered by student_id.
    """
    with get_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("""
                SELECT student_id, first_name, last_name, email, enrollment_date
                FROM students
                ORDER BY student_id;
            """)
            rows = cur.fetchall()
            print("\n== All Students ==")
            for r in rows:
                print(f"{r['student_id']:>3} | {r['first_name']} {r['last_name']} | {r['email']} | {r['enrollment_date']}")
            if not rows:
                print("(no rows)")

def addStudent(first_name, last_name, email, enrollment_date=None):
    """
    Create: Insert a new student and print the new student_id.
    Uses RETURNING to get the generated primary key.
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO students (first_name, last_name, email, enrollment_date)
                VALUES (%s, %s, %s, %s)
                RETURNING student_id;
            """, (first_name, last_name, email, enrollment_date))
            new_id = cur.fetchone()[0]
            conn.commit()
            print(f"Inserted student_id={new_id}")

def updateStudentEmail(student_id, new_email):
    """
    Update: Change the email of the given student_id.
    Prints whether a row was updated.
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                UPDATE students
                SET email = %s
                WHERE student_id = %s;
            """, (new_email, student_id))
            conn.commit()
            if cur.rowcount == 0:
                print(f"No student found with id={student_id}")
            else:
                print(f"Updated email for student_id={student_id} -> {new_email}")

def deleteStudent(student_id):
    """
    Delete: Remove a student by primary key.
    Prints whether a row was deleted.
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                DELETE FROM students
                WHERE student_id = %s;
            """, (student_id,))
            conn.commit()
            if cur.rowcount == 0:
                print(f"No student found with id={student_id}")
            else:
                print(f"Deleted student_id={student_id}")

# -------------
# Simple demo runner
# -------------

def demo():
    """
    Runs each function once so you can show it in your video
    and verify in pgAdmin after each step.
    """
    print("Testing DB connection and CRUD functions...\n")

    # 1) READ - should show your initial 3 rows
    getAllStudents()

    # 2) CREATE - insert a new student
    addStudent("Alice", "Wonder", "alice.wonder@example.com", "2023-09-03")
    getAllStudents()

    # 3) UPDATE - change Alice's email (find her id first)
    # We'll fetch the most recent row (highest id) for simplicity in this demo
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT max(student_id) FROM students;")
            newest_id = cur.fetchone()[0]

    updateStudentEmail(newest_id, "alice.w@example.com")
    getAllStudents()

    # 4) DELETE - remove the newest row
    deleteStudent(newest_id)
    getAllStudents()

if __name__ == "__main__":
    # You can run the scripted demo, or comment it out and call functions manually.
    demo()
