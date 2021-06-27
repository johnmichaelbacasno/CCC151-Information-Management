import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
from data.manager import connect

class Course:    
    def __init__(self, root):
        self.root = root
        self.root.title("Available Courses")
        self.root.geometry("575x575")
        self.root.resizable(width=False, height=False)
        self.root.configure(background="#FFFFFF")

        self.database = connect("data/database.db")
        
        self.course_code = tk.StringVar()
        self.course_name = tk.StringVar()
        
        self.clear()
        
        self.main = tk.Frame(self.root, bg="#FFFFFF")
        self.main.pack(fill="both")
        
        self.show()
    
    def show(self):
        self.main.forget()
        self.main = tk.Frame(self.root, bg="#FFFFFF")
        self.main.pack(fill="both")

        self.label_name = tk.Label(self.main, text="Available Courses", font=("Arial", 15), bg="#FFFFFF")
        self.label_name.pack(pady=20)

        self.frame_table = tk.Frame(self.root, bd=1)
        self.frame_table.pack(pady=15)
        
        self.table_heading = tk.Frame(self.frame_table, bg="#FFFFFF")
        self.table_heading.pack(fill="x")

        self.table_heading = tk.Frame(self.frame_table, bg="#FFFFFF")
        self.table_heading.pack(fill="x")
        
        self.heading_photo = tk.Label(self.table_heading, text="Course Code", font=("Arial", 8, "bold"), width=15, anchor="center", bg="#FFFFFF")
        self.heading_photo.grid(row=0, column=0, padx=10, pady=5)
        
        self.heading_roll = tk.Label(self.table_heading, text="Course Name", font=("Arial", 8, "bold"), width=25, anchor="center", bg="#FFFFFF")
        self.heading_roll.grid(row=0, column=1, padx=5, pady=5)
        
        self.heading_actions = tk.Label(self.table_heading, text="Actions", font=("Arial", 8, "bold"), width=8, anchor="center", bg="#FFFFFF")
        self.heading_actions.grid(row=0, column=2, padx=50, pady=5)
        
        self.table_line = tk.Frame(self.frame_table, height=2, bg="#D2D2D2")
        self.table_line.pack(fill="x")

        self.table_rows = ScrollableFrame(self.frame_table)
        self.table_rows.pack(fill="x")

        self.show_rows()

        self.bottom = tk.Frame(self.root, bg="#FFFFFF")
        self.bottom.pack(fill="both", padx=45)
        
        self.frame_id = tk.Frame(self.bottom, bg="#F3F4F6")
        self.frame_id.pack(fill="x")
        
        self.label_id = tk.Label(self.frame_id, text="Course Code", font=("Arial", 9, "bold"), width=15, anchor="w", bg="#F3F4F6")
        self.label_id.grid(row=0, column=0, padx=40, pady=10)
        
        self.entry_id = tk.Entry(self.frame_id, textvariable=self.course_code, font=("Arial", 9), width=32, bd=1.5, bg="#FFFFFF", highlightthickness=1, highlightbackground="grey", highlightcolor="dodgerblue1", relief="flat")
        self.entry_id.grid(row=0, column=1, padx=10, pady=0)
        
        self.frame_name = tk.Frame(self.bottom, bg="#FFFFFF")
        self.frame_name.pack(fill="x")
        
        self.label_name = tk.Label(self.frame_name, text="Course Name", font=("Arial", 9,"bold"), width=15, anchor="w", bg="#FFFFFF")
        self.label_name.grid(row=0, column=0, padx=40, pady=10)
        
        self.entry_name = tk.Entry(self.frame_name, textvariable=self.course_name, font=("Arial", 9), width=32, bd=1.5, bg="#FFFFFF", highlightthickness=1, highlightbackground="grey", highlightcolor="dodgerblue1", relief="flat")
        self.entry_name.grid(row=0, column=1, padx=10, pady=0)

        self.frame_buttons = tk.Frame(self.bottom, bg="#FFFFFF")
        self.frame_buttons.pack(pady=15)

        self.button_add = tk.Button(self.frame_buttons, command=self.add, text="Add", font=("Arial", 8, "bold"), width=8, bd=0, bg="#81C04B", fg="#FFFFFF", activebackground="#A1A1A1", activeforeground="#FFFFFF")
        self.button_add.grid(row=0, column=0, padx=10, pady=18)

        self.button_clear = tk.Button(self.frame_buttons, command=self.update, text="Update", font=("Arial", 8, "bold"), width=8, bd=0, bg="#11AFCA", fg="#FFFFFF", activebackground="#A1A1A1", activeforeground="#FFFFFF")
        self.button_clear.grid(row=0, column=1, padx=10, pady=18)
        
        self.button_close = tk.Button(self.frame_buttons, command=self.close, text="Close", font=("Arial", 8, "bold"), width=8, bd=0, bg="#F25658", fg="#FFFFFF", activebackground="#A1A1A1", activeforeground="#FFFFFF")
        self.button_close.grid(row=0, column=2, padx=10, pady=18)

    def show_rows(self):
        self.table_rows.forget()
        self.table_rows = ScrollableFrame(self.frame_table)
        self.table_rows.pack(fill="x")

        for row, data in enumerate(self.database.courses()):
            self.color = "#F3F4F6" if not row % 2 else "#FFFFFF"
            
            self.frame_row = tk.Frame(self.table_rows.scrollable_frame, bg=self.color)
            self.frame_row.pack(fill="x")
            
            self.row_name = tk.Label(self.frame_row, text=data[0], font=("Arial", 8), width=18, anchor="center", bg=self.color, fg="#6D99BC")
            self.row_name.grid(row=row, column=0, padx=5, pady=16)
            
            self.row_name = tk.Label(self.frame_row, text=data[1], font=("Arial", 8), width=32, anchor="center", bg=self.color)
            self.row_name.grid(row=row, column=1, padx=5, pady=16)
            
            self.button_delete = tk.Button(self.frame_row, command=lambda key=data[0]: self.delete(key), text="Delete", font=("Arial", 8, "bold"), width=8, bd=0, bg="#F25659", fg="#FFFFFF", activebackground = "#A1A1A1", activeforeground="#FFFFFF")
            self.button_delete.grid(row=row, column=2, padx=40, pady=16)

    def delete(self, key):
        if messagebox.askquestion("Delete Course", "Are you sure you want to delete this course?") == "yes":
            if self.database.exists_course(key):
                messagebox.showwarning("Delete Course", "Course cannot be deleted.")
            else:
                self.database.delete_course(key)
                messagebox.showinfo("Delete Course", "Course deleted.")
                self.show_rows()
    
    def add(self):       
        if messagebox.askquestion("Add Course", "Are you sure you want to add this course?") == "yes":
            if self.empty():
                messagebox.showwarning("Add Course", "Empty field not allowed.")
            else:
                if self.database.exists_course_code(self.course_code.get()):
                    self.course_code.set("")
                    messagebox.showwarning("Add Course", "Course already exists.")
                else:               
                    self.database.add_course(
                        self.course_code.get(),
                        self.course_name.get()
                    )
                    
                    messagebox.showinfo("Add Course", "Course added.")
                    self.show_rows()
    
    def update(self):       
        if messagebox.askquestion("Update Course", "Are you sure you want to update this course?") == "yes":
            if self.empty():
                messagebox.showwarning("Update Course", "Empty field not allowed.")
            else:
                if not self.database.exists_course_code(self.course_code.get()):
                    self.course_code.set("")
                    messagebox.showwarning("Update Course", "Course does not exist.")
                else:               
                    self.database.update_course(
                        course_code=self.course_code.get(),
                        course_name=self.course_name.get()
                    )
                    
                    messagebox.showinfo("Update Course", "Course updated.")
                    self.show_rows()
    
    def empty(self):
        return not (self.course_code.get() and self.course_name.get())

    def clear(self):
        self.course_code.set("")
        self.course_name.set("")     
    
    def close(self):
        if messagebox.askquestion("Courses", "Are you sure you want to close?") == "yes":
            self.database.exit()      
            self.root.destroy()

class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

if __name__ == "__main__":
    root = tk.Tk()
    main = Course(root)
    root.mainloop()
