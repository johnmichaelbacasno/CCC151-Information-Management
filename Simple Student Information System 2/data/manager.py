import itertools
import sqlite3

class connect:
    def __init__(self, file):
        self.con = sqlite3.connect(file)
        self.cur = self.con.cursor()
    
    def add(self, *info):
        self.cur.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?, ?)", info)
        self.save()

    def update(self, **info):
        self.cur.execute("UPDATE students SET name=:name, gender=:gender, course=:course, year=:year, birthdate=:birthdate, address=:address, contact=:contact WHERE id=:id", info)
        self.save()

    def delete(self, key):
        self.cur.execute("DELETE FROM students WHERE id=?", (key,))
        self.save()
    
    def display_row(self, id):
        return self.cur.execute(f"SELECT name, gender, course_name FROM students INNER JOIN courses ON students.course = courses.course_code WHERE id=?", (id,)).fetchone()

    def search_attr(self, id, attr):
        return self.cur.execute(f"SELECT {attr} FROM students WHERE id=?", (id,)).fetchone()[0]

    def search_by_id(self, key):
        return self.cur.execute("SELECT id FROM students WHERE id=?", (key,)).fetchone()

    def search_by_year(self, key):
        return tuple(itertools.chain(*self.cur.execute("SELECT id FROM students WHERE year=?", (key,)).fetchall()))

    def search_by_course(self, key):
        return tuple(itertools.chain(*self.cur.execute("SELECT id FROM students WHERE course=?", (key,)).fetchall()))

    def search_all(self):
        return tuple(itertools.chain(*self.cur.execute("SELECT id FROM students").fetchall()))
    
    def exists_id(self, key):
        return bool(self.cur.execute("SELECT id FROM students WHERE id=?", (key,)).fetchone())
    
    def exists_year(self, key):
        return bool(self.cur.execute("SELECT id FROM students WHERE year=?", (key,)).fetchone())
    
    def exists_course(self, key):
        return bool(self.cur.execute("SELECT id FROM students WHERE course=?", (key,)).fetchone())
    
    def exists_course_code(self, key):
        return bool(self.cur.execute("SELECT course_code FROM courses WHERE course_code=?", (key,)).fetchone())
    
    def exists_course_name(self, key):
        return bool(self.cur.execute("SELECT course_name FROM courses WHERE course_name=?", (key,)).fetchone())

    def courses(self):
        return tuple(itertools.chain(self.cur.execute("SELECT * FROM courses").fetchall()))
    
    def course_codes(self):
        return tuple(itertools.chain(*self.cur.execute("SELECT course_code FROM courses").fetchall()))

    def course_names(self):
        return tuple(itertools.chain(*self.cur.execute("SELECT course_name FROM courses").fetchall()))

    def add_course(self, *info):
        self.cur.execute("INSERT INTO courses VALUES (?, ?)", info)
        self.save()
    
    def update_course(self, **info):
        self.cur.execute("UPDATE courses SET course_name=:course_name WHERE course_code=:course_code", info)
        self.save()

    def delete_course(self, key):
        self.cur.execute("DELETE FROM courses WHERE course_code=?", (key,))
        self.save()
    
    def name_course(self, key):
        return self.cur.execute("SELECT course_name FROM courses WHERE course_code=?", (key,)).fetchone()[0]

    def length(self):
        return self.cur.execute("SELECT COUNT(*) FROM students").fetchone()[0]
    
    def save(self):
        self.con.commit()
    
    def exit(self):
        self.con.close()

if __name__ == "__main__":
    database = connect("database.db")
    print(database.courses())
