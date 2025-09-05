from tkinter import *
import tkinter
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System
from register import Register
from forgetpass import ForgetPass
import sys
        
class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        root.configure(bg="lightblue")
        self.root.wm_iconbitmap("facial_recognition.ico")
        sys.setrecursionlimit(2000)

        bg_image = Image.open("C:\\Users\\Rohan\\OneDrive\\Desktop\\Testing\\program_images\\loginbg.jpg")
        bg_image = bg_image.resize((1530, 790), Image.LANCZOS)  # Changed from Image.ANTIALIAS
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tkinter.Label(self.root, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.var_email = StringVar()
        self.var_password = StringVar()

        img1 = Image.open(r"C:\\Users\\Rohan\\OneDrive\\Desktop\\Testing\\program_images\\BVJNIOT.png")
        img1 = img1.resize((400, 160), Image.LANCZOS)  # Changed from Image.ANTIALIAS

        self.photoimage1 = ImageTk.PhotoImage(img1)
        tl2img1 = Label(image=self.photoimage1, borderwidth=0)
        tl2img1.place(x=550, y=0, width=500, height=165)
        
        get_str1 = Label(root, text="  Bharti Vidyapeeth's \n Jawaharlal Nehru Institute Of Technology", font=("times new roman", 30, "bold"), fg="black")
        get_str1.place(x=430, y=150)

        username = Label(root, text="Username :", font=("times new roman", 20, "bold"), fg="black")
        username.place(x=600, y=300)
        
        self.txtuser = Entry(root, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=750, y=305, width=270)

        password = Label(root, text="Password :", font=("times new roman", 20, "bold"), fg="black")
        password.place(x=600, y=370)

        self.txtpass = Entry(root, font=("times new roman", 15, "bold"))
        self.txtpass.place(x=750, y=375, width=270)

        loginbtn = Button(root, command=self.login, text="Login", font=("times new roman", 25, "bold"), bd=3,relief=RIDGE, fg="black", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=650, y=550, width=300, height=55)

        registerbtn = Button(root, text="New User Register", command=self.register_window,
                             font=("times new roman", 15, "bold"), borderwidth=0, fg="black",
                             activeforeground="white", activebackground="ivory")
        registerbtn.place(x=500, y=460, width=180, height=25)

        forgotbtn = Button(root, text="Forgot Password", command=self.forgot_pass_win,
                           font=("times new roman", 15, "bold"), borderwidth=0, fg="black",
                           activeforeground="white", activebackground="ivory")
        forgotbtn.place(x=900, y=460, width=180, height=25)

        img2 = Image.open(r"C:\\Users\\Rohan\\OneDrive\\Desktop\\Testing\\program_images\\lock1.png")
        img2 = img2.resize((30, 30), Image.LANCZOS)  # Changed from Image.ANTIALIAS
        self.photoimage2 = ImageTk.PhotoImage(img2)
        tl2img1 = Label(image=self.photoimage2, borderwidth=0)
        tl2img1.place(x=560, y=375, width=30, height=30)

        img3 = Image.open(r"C:\\Users\\Rohan\\OneDrive\\Desktop\\Testing\\program_images\\user.png")
        img3 = img3.resize((35, 35), Image.LANCZOS)  # Changed from Image.ANTIALIAS
        self.photoimage3 = ImageTk.PhotoImage(img3)
        tl2img1 = Label(image=self.photoimage3, borderwidth=0)
        tl2img1.place(x=560, y=305, width=30, height=30)

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All Fields Required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="root", database="student_data")
                my_cursor = conn.cursor()
            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"Connection error: {e}")
                return
            
            try:
                query = "select * from regteach where email=%s and pwd=%s"
                my_cursor.execute(query, (self.txtuser.get(), self.txtpass.get()))
                row = my_cursor.fetchone()
                
                if row is None:
                    messagebox.showerror("Error", "Invalid Username or Password")
                else:
                    open_main=messagebox.askyesno("YesNo", "Access Only Teacher")
                    if open_main>0:
                        self.scan = Toplevel(self.root)
                        self.app = Face_Recognition_System(self.scan)                    
                    else:
                        if not open_main:
                            return         
            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"Query execution error: {e}")
            finally:
                conn.commit()
                conn.close() 
                       
    def forgot_pass_win(self):
        self.scan = Toplevel(self.root)
        self.app = ForgetPass(self.scan)
        
    def Register(self,root):
        self.scan = Toplevel(self.root)
        self.app = Register(self.scan)
                
if __name__ == "__main__":
    root=Tk()
    app=Login_Window(root)
    root.mainloop()
