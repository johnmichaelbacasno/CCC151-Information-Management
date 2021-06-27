import random
import sqlite3

def student_generator():
    con = sqlite3.connect("database.db")
    cur = con.cursor()

    cur.execute("DELETE FROM students")

    students = []
    
    for year in range(1, 6):
        for count in range(1, 11):
            students.append((
                f"{2017 + year}-{str(count).zfill(4)}", 
                "First Name M. Last Name", 
                random.choice(["Male", "Female"]), 
                random.choice(["BSCS", "BSIT", "BSCA", "BSIS"]),
                year,
                f"{str(random.randint(1, 12)).zfill(2)}/{str(random.randint(1, 28)).zfill(2)}/{str(random.randint(1995, 2005))}",
                f"{random.choice(['Iligan', 'Cagayan'])} City",
                f"09{str(random.randint(1, 999999999)).zfill(9)}"
            ))

    cur.executemany("INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?, ?)", students)
    
    con.commit()
    con.close()

student_generator()
