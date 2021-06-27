import re
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
from data.manager import connect

class View:
    def __init__(self, root, key):
        self.root = root
        self.root.title("View Student")
        self.root.geometry("450x575")
        self.root.resizable(width=False, height=False)
        self.root.configure(background="#FFFFFF")
        
        self.key = key
        self.database = connect("data/database.db")
        self.image_student_male = ImageTk.PhotoImage(Image.open("res/student_male_icon.png"))
        self.image_student_female = ImageTk.PhotoImage(Image.open("res/student_female_icon.png"))
        self.image_student_generic = ImageTk.PhotoImage(Image.open("res/student_generic_icon.png"))
        
        self.id = tk.StringVar()
        self.name = tk.StringVar()
        self.gender = tk.StringVar()
        self.course = tk.StringVar()
        self.year = tk.StringVar()
        self.birthdate = tk.StringVar()  
        self.contact = tk.StringVar()
        self.address = tk.StringVar()
        
        self.clear()
        
        self.main = tk.Frame(self.root, bg="#FFFFFF")
        self.main.pack(fill="both")
        
        self.show()
    
    def show(self):
        self.id.set(self.database.search_attr(self.key, "id"))
        self.name.set(self.database.search_attr(self.key, "name"))
        self.gender.set(self.database.search_attr(self.key, "gender"))
        self.course.set(self.database.search_attr(self.key, "course"))
        self.year.set(self.database.search_attr(self.key, "year"))
        self.birthdate.set(self.database.search_attr(self.key, "birthdate"))
        self.contact.set(self.database.search_attr(self.key, "contact"))
        self.address.set(self.database.search_attr(self.key, "address"))
        
        self.main.forget()
        self.main = tk.Frame(self.root, bg="#FFFFFF")
        self.main.pack(fill="both")
        
        self.frame_photo = tk.Frame(self.main, bg="#FFFFFF")
        self.frame_photo.pack(fill="x")
        
        if self.gender.get() == "Male":
            self.image_student = self.image_student_male 
        elif self.gender.get() == "Female":
            self.image_student = self.image_student_female
        else:
            self.image_student = self.image_student_generic
        
        self.label_photo = tk.Label(self.frame_photo, image=self.image_student, width=10, anchor="center", bg="#FFFFFF",)
        self.label_photo.pack(side="top", fill="both", pady=15)
        
        self.frame_id = tk.Frame(self.main, bg="#F3F4F6")
        self.frame_id.pack(fill="x")
        
        self.label_id = tk.Label(self.frame_id, text="ID Number", font=("Arial", 9, "bold"), width=10, anchor="w", bg="#F3F4F6")
        self.label_id.grid(row=0, column=0, padx=40, pady=10)
        
        self.entry_id = tk.Entry(self.frame_id, textvariable=self.id, font=("Arial", 9), width=30, bd=1.5, bg="#FFFFFF", highlightthickness=1, highlightbackground="grey", highlightcolor="dodgerblue1", relief="flat", state="disabled", disabledbackground="#FFFFFF", disabledforeground="#000000")
        self.entry_id.grid(row=0, column=1, padx=10, pady=10)
        
        self.frame_name = tk.Frame(self.main, bg="#FFFFFF")
        self.frame_name.pack(fill="x")
        
        self.label_name = tk.Label(self.frame_name, text="Name", font=("Arial", 9,"bold"), width=10, anchor="w", bg="#FFFFFF")
        self.label_name.grid(row=0, column=0, padx=40, pady=10)
        
        self.entry_name = tk.Entry(self.frame_name, textvariable=self.name, font=("Arial", 9), width=30, bd=1.5, bg="#FFFFFF", highlightthickness=1, highlightbackground="grey", highlightcolor="dodgerblue1", relief="flat")
        self.entry_name.grid(row=0, column=1, padx=10, pady=10)
        
        self.frame_gender = tk.Frame(self.main, bg="#F3F4F6")
        self.frame_gender.pack(fill="x")
        
        self.label_gender = tk.Label(self.frame_gender, text="Gender", font=("Arial", 9, "bold"), width=10, anchor="w", bg="#F3F4F6")
        self.label_gender.grid(row=0, column=0, padx=40, pady=10)
        
        # self.entry_gender = tk.Entry(self.frame_gender, textvariable=self.gender, font=("Arial", 9), width=30, bd=1.5, bg="#FFFFFF", highlightthickness=1, highlightbackground="grey", highlightcolor="dodgerblue1", relief="flat")
        # self.entry_gender.grid(row=0, column=1, padx=10, pady=10)

        self.entry_gender = ttk.Combobox(self.frame_gender, textvariable=self.gender, values=("Male", "Female"), width=28, font=("Arial", 9))
        self.entry_gender.grid(row=0, column=1, padx=10, pady=10)
        
        self.frame_course = tk.Frame(self.main, bg="#FFFFFF")
        self.frame_course.pack(fill="x")
        
        self.label_course = tk.Label(self.frame_course, text="Course", font=("Arial", 9,"bold"), width=10, anchor="w", bg="#FFFFFF")
        self.label_course.grid(row=0, column=0, padx=40, pady=10)
        
        # self.entry_course = tk.Entry(self.frame_course, textvariable=self.course, font=("Arial", 9), width=30, bd=1.5, bg="#FFFFFF", highlightthickness=1, highlightbackground="grey", highlightcolor="dodgerblue1", relief="flat")
        # self.entry_course.grid(row=0, column=1, padx=10, pady=10)

        self.entry_course = ttk.Combobox(self.frame_course, textvariable=self.course, values=self.database.course_codes(), width=28, font=("Arial", 9), state="readonly")
        self.entry_course.grid(row=0, column=1, padx=10, pady=10)
        
        self.frame_year = tk.Frame(self.main, bg="#F3F4F6")
        self.frame_year.pack(fill="x")
        
        self.label_year = tk.Label(self.frame_year, text="Year Level", font=("Arial", 9, "bold"), width=10, anchor="w", bg="#F3F4F6")
        self.label_year.grid(row=0, column=0, padx=40, pady=10)
        
        # self.entry_year = tk.Entry(self.frame_year, textvariable=self.year, font=("Arial", 9), width=30, bd=1.5, bg="#FFFFFF", highlightthickness=1, highlightbackground="grey", highlightcolor="dodgerblue1", relief="flat")
        # self.entry_year.grid(row=0, column=1, padx=10, pady=10)

        self.entry_year = ttk.Combobox(self.frame_year, textvariable=self.year, values=("1", "2", "3", "4", "5"), width=28, font=("Arial", 9), state="readonly")
        self.entry_year.grid(row=0, column=1, padx=10, pady=10)
        
        self.frame_birthdate = tk.Frame(self.main, bg="#FFFFFF")
        self.frame_birthdate.pack(fill="x")
        
        self.label_birthdate = tk.Label(self.frame_birthdate, text="Birthdate", font=("Arial", 9,"bold"), width=10, anchor="w", bg="#FFFFFF")
        self.label_birthdate.grid(row=0, column=0, padx=40, pady=10)
        
        self.entry_birthdate = tk.Entry(self.frame_birthdate, textvariable=self.birthdate, font=("Arial", 9), width=30, bd=1.5, bg="#FFFFFF", highlightthickness=1, highlightbackground="grey", highlightcolor="dodgerblue1", relief="flat")
        self.entry_birthdate.grid(row=0, column=1, padx=10, pady=10)
        
        self.frame_address = tk.Frame(self.main, bg="#F3F4F6")
        self.frame_address.pack(fill="x")
        
        self.label_address = tk.Label(self.frame_address, text="Address", font=("Arial", 9, "bold"), width=10, anchor="w", bg="#F3F4F6")
        self.label_address.grid(row=0, column=0, padx=40, pady=10)
        
        self.entry_address = tk.Entry(self.frame_address, textvariable=self.address, font=("Arial", 9), width=30, bd=1.5, bg="#FFFFFF", highlightthickness=1, highlightbackground="grey", highlightcolor="dodgerblue1", relief="flat")
        self.entry_address.grid(row=0, column=1, padx=10, pady=10)
        
        self.frame_contact = tk.Frame(self.main, bg="#FFFFFF")
        self.frame_contact.pack(fill="x")
        
        self.label_contact = tk.Label(self.frame_contact, text="Contact", font=("Arial", 9,"bold"), width=10, anchor="w", bg="#FFFFFF")
        self.label_contact.grid(row=0, column=0, padx=40, pady=10)
        
        self.entry_contact = tk.Entry(self.frame_contact, textvariable=self.contact, font=("Arial", 9), width=30, bd=1.5, bg="#FFFFFF", highlightthickness=1, highlightbackground="grey", highlightcolor="dodgerblue1", relief="flat")
        self.entry_contact.grid(row=0, column=1, padx=10, pady=10)
       
        self.frame_buttons = tk.Frame(self.main, bg="#FFFFFF")
        self.frame_buttons.pack(pady=5)
        
        self.button_update = tk.Button(self.frame_buttons, command=self.update, text="Update", font=("Arial", 8, "bold"), width=8, bd=0, bg="#81C04B", fg="#FFFFFF", activebackground="#A1A1A1", activeforeground="#FFFFFF")
        self.button_update.grid(row=0, column=0, padx=10, pady=15)
        
        self.button_clear = tk.Button(self.frame_buttons, command=self.clear, text="Clear", font=("Arial", 8, "bold"), width=8, bd=0, bg="#11AFCA", fg="#FFFFFF", activebackground="#A1A1A1", activeforeground="#FFFFFF")
        self.button_clear.grid(row=0, column=1, padx=10, pady=15)
        
        self.button_close = tk.Button(self.frame_buttons, command=self.close, text="Close", font=("Arial", 8, "bold"), width=8, bd=0, bg="#F25658", fg="#FFFFFF", activebackground="#A1A1A1", activeforeground="#FFFFFF")
        self.button_close.grid(row=0, column=2, padx=10, pady=15)
    
    def update(self):
        if self.empty():
            messagebox.showwarning("Update Student", "Empty field not allowed.")
        elif self.match():
            self.database.update(
                id=self.id.get(),
                name=self.name.get(),
                gender=self.gender.get().capitalize(),
                course=self.course.get(),
                year=int(self.year.get()),
                birthdate=self.birthdate.get(),
                address=self.address.get(),
                contact=self.contact.get()
            )

            if messagebox.askquestion("Update Student", "Are you sure you want to update this student?") == "yes":
                messagebox.showinfo("Update Student", "Student updated.")
                self.show()
    
    def clear(self):
        self.name.set("")
        self.gender.set("")
        self.course.set("")
        self.year.set("")
        self.birthdate.set("")
        self.contact.set("")
        self.address.set("")      
    
    def close(self):
        if messagebox.askquestion("View Student", "Are you sure you want to close?") == "yes":
            self.database.exit()    
            self.root.destroy()
    
    def empty(self):
        return not (self.id.get() and self.name.get() and self.gender.get() and 
                    self.course.get() and self.year.get() and self.birthdate.get() and 
                    self.contact.get() and self.address.get())

    def match(self):
        self.message = ""
        self.mismatch = 0    
        self.regex_id = r"\d\d\d\d-\d\d\d\d"
        self.regex_name = r"([a-zA-Z]+[ \"-]?)+ [A-Z]. ([a-zA-Z]+[ \"-]?)+"
        self.regex_year = r"[12345]"
        self.regex_birthdate = r"\d\d/\d\d/\d\d\d\d"
        
        if not re.fullmatch(self.regex_id, self.id.get()):
            self.id.set("")
            self.message += "\n\nID NUMBER\nMust be \"dddd-dddd\"."
            self.mismatch += 1
        
        if not re.fullmatch(self.regex_name, self.name.get()):
            self.name.set("")
            self.message += "\n\nNAME\nMust be \"[first-name] [middle-initial]. [last-name]\"."
            self.mismatch += 1
        
        if not re.fullmatch(self.regex_year, self.year.get()):
            self.year.set("")
            self.message += "\n\nYEAR LEVEL\nMust be between \"1 ~ 5\"."
            self.mismatch += 1
        
        if not re.fullmatch(self.regex_birthdate, self.birthdate.get()):
            self.birthdate.set("")
            self.message += "\n\nBIRTHDATE\nMust be \"DD/MM/YYYY\"."
            self.mismatch += 1
        
        if not self.database.exists_course_code(self.course.get()):
            self.course.set("")
            self.message += "\n\nCOURSE\nMust be found in \"available courses\"."
            self.mismatch += 1
        
        if self.mismatch:
            self.message = f"There are {self.mismatch} mismatches found.{self.message}"
            messagebox.showerror("View Student", self.message)
            return False
        
        return True

if __name__ == "__main__":
    root = tk.Tk()
    main = View(root, "2019-0001")
    root.mainloop()
