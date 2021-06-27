import sqlite3

con = sqlite3.connect("database.db")
cur = con.cursor()

cur.executescript("""

    CREATE TABLE students(
        id CHAR(9) NOT NULL PRIMARY KEY,
        name VCHAR(25) NOT NULL,
        gender VCHAR(15) NOT NULL,
        course VCHAR(5) NOT NULL,
        year INTEGER NOT NULL,
        birthdate CHAR(10) NOT NULL,
        address VCHAR(50) NOT NULL,
        contact VCHAR(50) NOT NULL,
        FOREIGN KEY (course) REFERENCES courses (course_code)
    );
    
    CREATE TABLE courses(
        course_code VCHAR(5) NOT NULL PRIMARY KEY,
        course_name VCHAR(25) NOT NULL
    );

    INSERT INTO courses VALUES("BSCS", "BS Computer Science");
    INSERT INTO courses VALUES("BSIT", "BS Information Technology");
    INSERT INTO courses VALUES("BSCA", "BS Computer Application");
    INSERT INTO courses VALUES("BSIS", "BS Information Systems");

""")

con.commit()
con.close()
