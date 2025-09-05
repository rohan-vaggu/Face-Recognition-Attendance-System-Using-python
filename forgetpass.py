from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
import sys

class ForgetPass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("750x600+0+0")
        self.root.title("Forget Password")
        sys.setrecursionlimit(2000)

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        width = 750
        height = 600

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.root.geometry(f'{width}x{height}+{x}+{y}')

        self.var_ssq = StringVar()

        tl8 = Label(self.root, text="Forget Password", font=("algerian", 30, "bold"), fg="red", bg="chartreuse")
        tl8.place(x=0, y=10, relwidth=1)

        label_frame3 = Label(self.root, text="Email id: ", font=("times new roman", 20, "bold"), fg="black")
        label_frame3.place(x=50, y=150)

        self.txt_frame3 = ttk.Entry(self.root, font=("times new roman", 15, "bold"))
        self.txt_frame3.place(x=350, y=150, width=250)

        label_frame4 = Label(self.root, text="Select security question: ", font=("times new roman", 20, "bold"))
        label_frame4.place(x=50, y=220)

        self.combo_security = ttk.Combobox(root, textvariable=self.var_ssq, font=("times new roman", 15, "bold"), state="readonly")
        self.combo_security["values"] = ("Select", "Your Date of Birth", "Your Nick Name", "Your Favorite Book")
        self.combo_security.current(0)
        self.combo_security.place(x=350, y=220, width=250)

        new_pass = Label(self.root, text="New Password : ", font=("times new roman", 20, "bold"), fg="black")
        new_pass.place(x=50, y=360)

        self.txt_newpass = ttk.Entry(self.root, font=("times new roman", 15, "bold"))
        self.txt_newpass.place(x=350, y=360, width=250)

        new_confpass = Label(self.root, text="Confirm Password : ", font=("times new roman", 20, "bold"), fg="black")
        new_confpass.place(x=50, y=430)

        self.txt_confnewpass = ttk.Entry(self.root, font=("times new roman", 15, "bold"))
        self.txt_confnewpass.place(x=350, y=430, width=250)

        security_ans = Label(self.root, text="Security answer: ", font=("times new roman", 20, "bold"), fg="black")
        security_ans.place(x=50, y=290)

        self.txt_frame4 = ttk.Entry(self.root, font=("times new roman", 15, "bold"))
        self.txt_frame4.place(x=350, y=290, width=250)

        btn = Button(self.root, text="Reset", font=("times new roman", 25, "bold"), command=self.reset_pass)
        btn.place(x=280, y=500, width=150, height=35)

    def reset_pass(self):
        email = self.txt_frame3.get()
        security_question = self.combo_security.get()
        new_password = self.txt_newpass.get()
        confirm_password = self.txt_confnewpass.get()
        security_answer = self.txt_frame4.get()

        if not email:
            messagebox.showerror("Error", "Please enter your email")
            return

        if not (security_question and new_password and confirm_password and security_answer):
            messagebox.showerror("Error", "Please fill all fields")
            return

        if new_password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
            return

        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="root", database="student_data")
            my_cursor = conn.cursor()

            my_cursor.execute("SELECT sa FROM regteach WHERE email = %s AND ssq = %s", (email, security_question))
            result = my_cursor.fetchone()
            if result is None:
                messagebox.showerror("Error", "Invalid security question or answer")
                conn.close()
                return

            my_cursor.execute("UPDATE regteach SET pwd = %s WHERE email = %s", (new_password, email))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Password reset successful")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = Tk()
    app = ForgetPass(root)
    root.mainloop()
