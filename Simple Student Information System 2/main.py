import math
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
from data.manager import connect
from view import View
from add import Add
from course import Course

class Main:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Student Information System 2")
        self.root.geometry("875x575")
        self.root.resizable(width=False, height=False)
        self.root.configure(background="#FFFFFF")
        
        self.database = connect("data/database.db")
        self.image_student_male = ImageTk.PhotoImage(Image.open("res/student_male_icon_small.png"))
        self.image_student_female = ImageTk.PhotoImage(Image.open("res/student_female_icon_small.png"))
        self.image_student_generic = ImageTk.PhotoImage(Image.open("res/student_generic_icon_small.png"))
        
        self.search_result = tk.StringVar()
        self.search_category = tk.StringVar()
        self.search_category.set("ID")
        
        self.show()
    
    def show(self):
        self.frame_top = tk.Frame(self.root, height=50, bg="#FFFFFF")
        self.frame_top.pack(fill="x")
        
        self.frame_search = tk.Frame(self.frame_top, bg="#FFFFFF")
        self.frame_search.place(x=33, y=15)
        
        self.label_search = tk.Label(self.frame_search, text="Search by:", font=("Arial", 8), anchor="center", bg="#FFFFFF")
        self.label_search.pack(side="left", padx=5)

        self.drop_search = ttk.Combobox(self.frame_search, textvariable=self.search_category, values=("ID", "Year", "Course"), width=8, font=("Arial", 8), state="readonly")
        self.drop_search.pack(side="left", padx=5)
        
        self.entry_search = tk.Entry(self.frame_search, font=("Arial", 8), justify="center", width=15, textvariable=self.search_result, bd=1, bg="#FFFFFF", highlightthickness=1, highlightbackground="grey", highlightcolor="dodgerblue1", relief="flat")
        self.entry_search.pack(side="left", padx=8)
        
        self.button_go = tk.Button(self.frame_search, command=lambda: self.search_by_category(self.search_result.get()), text="Go", font=("Arial", 8, "bold"), width=5, bd=0, bg="#11AFCA", fg="#FFFFFF", activebackground = "#A1A1A1", activeforeground="#FFFFFF")
        self.button_go.pack(side="left", padx=5)
        
        self.button_all = tk.Button(self.frame_search, command=self.search_all, text="All", font=("Arial", 8, "bold"), width=5, bd=0, bg="#F25659", fg="#FFFFFF", activebackground = "#A1A1A1", activeforeground="#FFFFFF")
        self.button_all.pack(side="left", padx=5)

        self.button_course = tk.Button(self.frame_search, command=self.open_course, text="Courses", font=("Arial", 8, "bold"), width=8, bd=0, bg="#81C04B", fg="#FFFFFF", activebackground = "#A1A1A1", activeforeground="#FFFFFF")
        self.button_course.pack(side="left", padx=5)
        
        self.button_add = tk.Button(self.frame_top, command=self.open_add, text="+    Add New", font=("Arial", 8, "bold"), width=14, bd=0, bg="#81C04B", fg="#FFFFFF", activebackground = "#A1A1A1", activeforeground="#FFFFFF")
        self.button_add.place(x=733, y=15)
        
        self.frame_center = tk.Frame(self.root, height=460, bg="#FFFFFF")
        self.frame_center.pack(fill="x")
        self.frame_center.pack_propagate(False)
        
        self.frame_table = tk.Frame(self.frame_center, bd=1)
        self.frame_table.place(x=32, y=10)
        
        self.table_heading = tk.Frame(self.frame_table, bg="#FFFFFF")
        self.table_heading.pack(fill="x")
        
        self.heading_photo = tk.Label(self.table_heading, text="Photo", font=("Arial", 8, "bold"), width=15, anchor="center", bg="#FFFFFF")
        self.heading_photo.grid(row=0, column=0, padx=10, pady=5)
        
        self.heading_roll = tk.Label(self.table_heading, text="ID Number", font=("Arial", 8, "bold"), width=8, anchor="center", bg="#FFFFFF")
        self.heading_roll.grid(row=0, column=1, padx=10, pady=5)
        
        self.heading_name = tk.Label(self.table_heading, text="Student Name", font=("Arial", 8, "bold"), width=25, anchor="center", bg="#FFFFFF")
        self.heading_name.grid(row=0, column=2, padx=10, pady=5)
        
        self.heading_course = tk.Label(self.table_heading, text="Course", font=("Arial", 8, "bold"), width=20, anchor="center",  bg="#FFFFFF")
        self.heading_course.grid(row=0, column=3, padx=10, pady=5)
        
        self.heading_actions = tk.Label(self.table_heading, text="Actions", font=("Arial", 8, "bold"), width=22, anchor="center", bg="#FFFFFF")
        self.heading_actions.grid(row=0, column=4, padx=35, pady=5)
        
        self.table_line = tk.Frame(self.frame_table, height=2, bg="#D2D2D2")
        self.table_line.pack(fill="x")
        
        self.table_rows = tk.Frame(self.frame_table)
        self.table_rows.pack(fill="x")
        
        self.frame_bottom = tk.Frame(self.root, bg="#FFFFFF")
        self.frame_bottom.pack(fill="x")

        self.frame_navigation = tk.Frame(self.frame_bottom, bg="#FFFFFF")
        self.frame_navigation.pack(pady=10)
        
        self.search_all()

    def show_rows(self):
        self.start = (self.entry_number - 1) * 5
        self.table_rows.forget()
        self.table_rows = tk.Frame(self.frame_table)
        self.table_rows.pack(fill="x")
        
        for row, key in enumerate(self.results[self.start:self.start+5]):
            
            self.name, self.gender, self.course = self.database.display_row(key)
            self.color = "#F3F4F6" if not row % 2 else "#FFFFFF"
            
            if self.gender == "Male":
                self.image_student = self.image_student_male
            elif self.gender == "Female":
                self.image_student = self.image_student_female
            else:
                self.image_student = self.image_student_generic
            
            self.frame_row = tk.Frame(self.table_rows, bg=self.color)
            self.frame_row.pack(fill="x")
            
            self.row_photo = tk.Label(self.frame_row, image=self.image_student, width=107, anchor="center", bg=self.color,)
            self.row_photo.grid(row=row, column=0, padx=10, pady=0)
            
            self.row_roll = tk.Label(self.frame_row, text=key, font=("Arial", 8), width=9, anchor="center", bg=self.color, fg="#6D99BC")
            self.row_roll.grid(row=row, column=1, padx=12, pady=30)
            
            self.row_name = tk.Label(self.frame_row, text=self.name, font=("Arial", 8), width=29, anchor="center", bg=self.color)
            self.row_name.grid(row=row, column=2, padx=10, pady=20)
            
            self.row_course = tk.Label(self.frame_row, text=self.course, font=("Arial", 8), width=23, anchor="center",  bg=self.color)
            self.row_course.grid(row=row, column=3, padx=10, pady=20)
            
            self.action_buttons = tk.Frame(self.frame_row, bg=self.color)
            self.action_buttons.grid(row=row, column=4, padx=33)
            
            self.button_view = tk.Button(self.action_buttons, command=lambda key=key: self.open_view(key), text="View", font=("Arial", 8, "bold"), width=8, bd=0, bg="#11AFCA", fg="#FFFFFF", activebackground = "#A1A1A1", activeforeground="#FFFFFF")
            self.button_view.grid(row=row, column=0, padx=10, pady=10)
            
            self.button_delete = tk.Button(self.action_buttons, command=lambda key=key: self.delete(key), text="Delete", font=("Arial", 8, "bold"), width=8, bd=0, bg="#F25659", fg="#FFFFFF", activebackground = "#A1A1A1", activeforeground="#FFFFFF")
            self.button_delete.grid(row=row, column=1, padx=10, pady=10)

    def show_navigation(self):
        self.frame_navigation.forget()
        self.frame_navigation = tk.Frame(self.frame_bottom, bg="#FFFFFF")
        self.frame_navigation.pack(pady=10)
        
        self.button_previous = tk.Button(self.frame_navigation, command=self.previous, text="<", font=("Arial", 8, "bold"), bd=0, bg="#FFFFFF", fg="#000000", activebackground = "#D2D2D2", activeforeground="#FFFFFF")
        self.button_previous.grid(row=0, column=0)
        
        self.label_entry = tk.Label(self.frame_navigation, text=str(self.entry_number), font=("Arial", 8), width=8, height=2, anchor="center", bg="#F3F4F6")
        self.label_entry.grid(row=0, column=1)
        
        self.button_next = tk.Button(self.frame_navigation, command=self.next, text=">", font=("Arial", 8, "bold"), bd=0, bg="#FFFFFF", fg="#000000", activebackground = "#D2D2D2", activeforeground="#FFFFFF")
        self.button_next.grid(row=0, column=2)

    def search_all(self):
        self.results = self.database.search_all()
        self.entry_count = math.ceil(len(self.results) / 5)
        self.entry_number = 1
        self.show_rows()
        self.show_navigation()

    def search_by_category(self, key):
        if self.search_category.get() == "ID":
            self.search_by_id(key)
        elif self.search_category.get() == "Year":
            self.search_by_year(key)
        elif self.search_category.get() == "Course":
            self.search_by_course(key)
    
    def search_by_id(self, key):
        if not key:
            tk.messagebox.showerror("Search by ID", "Field required.")
        elif not self.database.exists_id(key):
            tk.messagebox.showerror("Search by ID", "No student found.")
        else:
            self.results = (key,)
            self.entry_count = 1
            self.entry_number = 1
            self.show_rows()
            self.show_navigation()
    
    def search_by_year(self, key):
        if not key:
            tk.messagebox.showerror("Search by Year", "Field required.")
        elif not self.database.exists_year(key):
            tk.messagebox.showerror("Search by Year", "No student found.")
        else:
            self.results = self.database.search_by_year(key)
            self.entry_count = math.ceil(len(self.results) / 5)
            self.entry_number = 1
            self.show_rows()
            self.show_navigation()
    
    def search_by_course(self, key):
        if not key:
            tk.messagebox.showerror("Search by Course", "Field required.")
        elif not self.database.exists_course(key):
            tk.messagebox.showerror("Search by Course", "No student found.")
        else:
            self.results = self.database.search_by_course(key)
            self.entry_count = math.ceil(len(self.results) / 5)
            self.entry_number = 1
            self.show_rows()
            self.show_navigation()
    
    def delete(self, key):
        if messagebox.askquestion("Delete Student", "Are you sure you want to delete this student?") == "yes":
            self.database.delete(key)
            messagebox.showinfo("Delete Student", "Student deleted.")
            self.search_all()
    
    def previous(self):
        if self.entry_number > 1:
            self.entry_number -= 1
            self.show_rows()
            self.show_navigation()
    
    def next(self):
        if self.entry_number < self.entry_count:
            self.entry_number += 1
            self.show_rows()
            self.show_navigation()
    
    def open_view(self, key):
        self.window_view = View(tk.Toplevel(self.root), key)
    
    def open_add(self):
        self.window_add = Add(tk.Toplevel(self.root))
    
    def open_course(self):
        self.window_course = Course(tk.Toplevel(self.root))

if __name__ == "__main__":
    root = tk.Tk()
    main = Main(root)
    root.mainloop()
