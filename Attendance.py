from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import pandas as pd
import sys

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Online Face Recognition System")
        root.configure(bg="lightblue")   
        sys.setrecursionlimit(2000)     

        # Title Label
        t1 = Label(root, text="View Attendance", font=("Garamond", 35, "bold"), bg="lightblue", fg="black")
        t1.place(x=0, y=0, width=1535, height=100)

        main_fram = LabelFrame(root, text="View Attendance", bd=2, bg="lightblue", font=("Garamond", 14, "bold"), fg="red")
        main_fram.place(x=5, y=100, width=1523, height=620)

        # Create a button to open the file manager
        extract_button = Button(root, text="Extract CSV File", command=self.open_file_manager, bg="blue", fg="white", font=("Garamond", 15, "bold"))
        extract_button.place(x=700, y=730, width=180, height=40)

        Scroll_x = ttk.Scrollbar(main_fram, orient=HORIZONTAL)
        Scroll_y = ttk.Scrollbar(main_fram, orient=VERTICAL)

        self.Attendance_table = ttk.Treeview(main_fram, column=("Name", "Department", "Year", "Enrollment number", "Roll Number","Date","Time", "Status"),
                                             xscrollcommand=Scroll_x.set, yscrollcommand=Scroll_y.set)

        Scroll_x.pack(side=BOTTOM, fill=X)
        Scroll_y.pack(side=RIGHT, fill=Y)

        Scroll_x.config(command=self.Attendance_table.xview)
        Scroll_y.config(command=self.Attendance_table.yview)

        self.Attendance_table.heading("Name", text="Name", anchor="center")
        self.Attendance_table.heading("Department", text="Department", anchor="center")
        self.Attendance_table.heading("Year", text="Year", anchor="center")
        self.Attendance_table.heading("Enrollment number", text="Enrollment Number", anchor="center")
        self.Attendance_table.heading("Roll Number", text="Roll Number", anchor="center")
        self.Attendance_table.heading("Date", text="Date", anchor="center")
        self.Attendance_table.heading("Time", text="Time", anchor="center")
        self.Attendance_table.heading("Status", text="Status", anchor="center")
        self.Attendance_table["show"] = "headings"

        self.Attendance_table.column("Name", width=300, anchor="center")
        self.Attendance_table.column("Department", width=100, anchor="center")
        self.Attendance_table.column("Year", width=100, anchor="center")
        self.Attendance_table.column("Enrollment number", width=100, anchor="center")
        self.Attendance_table.column("Roll Number", width=100, anchor="center")
        self.Attendance_table.column("Date", width=100, anchor="center")
        self.Attendance_table.column("Time", width=100, anchor="center")
        self.Attendance_table.column("Status", width=100, anchor="center")

        self.Attendance_table.pack(fill=BOTH, expand=1)

    def open_file_manager(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

        if file_path:
            try:
                df = pd.read_csv(file_path)

                for i in self.Attendance_table.get_children():
                    self.Attendance_table.delete(i)

                for index, row in df.iterrows():
                    self.Attendance_table.insert("", "end", values=(row["Name"], row["Course"], row["Year"],
                                                                    row["Enrollment"], row["Roll_no"], row["Date"], 
                                                                    row["Time"],row["Status"]))

            except pd.errors.EmptyDataError:
                messagebox.showerror("Error", "The selected CSV file is empty.")
            except pd.errors.ParserError:
                messagebox.showerror("Error", "Unable to parse the selected file. Please check if it's a valid CSV file.")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
