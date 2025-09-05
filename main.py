from tkinter import *
import tkinter
from PIL import Image, ImageTk
from addface import addface
from tkinter import messagebox
from Attendance import Attendance
from chatbot import Chatbot
from developers import Developers
import PyPDF2
from datetime import datetime
import cv2
import os
import mysql.connector
import sys
from helpandsupport import Helpandsupport

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")
        sys.setrecursionlimit(2000)
        

        bg_image = Image.open("C:\\Users\\Rohan\\OneDrive\\Desktop\\Testing\\program_images\\bg10.jpg")
        bg_image = bg_image.resize((1530, 790), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tkinter.Label(self.root, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)  

        # Title Label
        tl1 = Label(root, text="FACE RECOGNITION ATTENDANCE\n SYSTEM", font=("Garamond", 35, "bold"), fg="white", bg="black")
        tl1.place(x=320, y=30, width=1000, height=85)

        # Add Face button
        img1 = Image.open("C:\\Users\\Rohan\\OneDrive\\Desktop\\Testing\\program_images\\AddFaceButton.png")
        img1 = img1.resize((200, 200))
        self.photoimage2 = ImageTk.PhotoImage(img1)

        Add_face = Button(self.root, image=self.photoimage2, command=self.open_second_window, cursor="hand2")
        Add_face.place(x=200, y=200, width=180, height=180)

        b1 = Label(self.root, text="Student Details", font=("Garamond", 15, "bold"))
        b1.place(x=200, y=380, width=180, height=50)

        # Take Attendance Button
        img3 = Image.open("C:\\Users\\Rohan\\OneDrive\\Desktop\\Testing\\program_images\\TakeAttendanceButton.jpg")
        img3 = img3.resize((200, 200))
        self.photoimage3 = ImageTk.PhotoImage(img3)

        Take_Attendance = Button(self.root, image=self.photoimage3, command=self.f_recog, cursor="hand2")
        Take_Attendance.place(x=512, y=200, width=180, height=180)

        b2 = Label(self.root, text="Take Attendance", cursor="hand2", font=("Garamond", 15, "bold"))
        b2.place(x=512, y=380, width=180, height=50)

        # View Attendance
        img4 = Image.open("C:\\Users\\Rohan\\OneDrive\\Desktop\\Testing\\program_images\\Checkattendancebutton.jpg")
        img4 = img4.resize((200, 200))
        self.photoimage4 = ImageTk.PhotoImage(img4)

        View_attendance = Button(self.root, image=self.photoimage4, command=self.Attendance, cursor="hand2")
        View_attendance.place(x=825, y=200, width=180, height=180)

        b3 = Label(self.root, text="View Attendance", cursor="hand2", font=("Garamond", 15, "bold"))
        b3.place(x=825, y=380, width=180, height=50)

        # Exit button
        img5 = Image.open("C:\\Users\\Rohan\\OneDrive\\Desktop\\Testing\\program_images\\ExitButton.jpg")
        img5 = img5.resize((200, 200))
        self.photoimage5 = ImageTk.PhotoImage(img5)

        Exit_Button = Button(self.root, image=self.photoimage5, command=self.exit_button, cursor="hand2")
        
        Exit_Button.place(x=1150, y=500, width=180, height=180)


        b4 = Label(self.root, text="Exit", cursor="hand2", font=("Garamond", 15, "bold"))
        
        b4.place(x=1150, y=680, width=180, height=50)

        # User Manual
        img6 = Image.open("C:\\Users\\Rohan\\OneDrive\\Desktop\\Testing\\program_images\\usermanual.png")
        img6 = img6.resize((200, 200))
        self.photoimage6 = ImageTk.PhotoImage(img6)

        Manual = Button(self.root, image=self.photoimage6, command=self.read_pdf, cursor="hand2")
        Manual.place(x=1150, y=200, width=180, height=180)

        b5 = Label(self.root, text="User Manual", cursor="hand2", font=("Garamond", 15, "bold"))
        b5.place(x=1150, y=380, width=180, height=50)

        # Developer
        img7 = Image.open("C:\\Users\\Rohan\\OneDrive\\Desktop\\Testing\\program_images\\AboutDeveloper.png")
        img7 = img7.resize((200, 200))
        self.photoimage7 = ImageTk.PhotoImage(img7)

        Manual = Button(self.root, image=self.photoimage7, command=self.programmers, cursor="hand2")
        Manual.place(x=825, y=500, width=180, height=180)

        b6 = Label(self.root, text="About Developers", cursor="hand2", font=("Garamond", 15, "bold"))
        b6.place(x=825, y=680, width=180, height=50)

        # Chat bot
        img8 = Image.open("C:\\Users\\Rohan\\OneDrive\\Desktop\\Testing\\program_images\\chatbot.jpg")
        img8 = img8.resize((200, 200))
        self.photoimage8 = ImageTk.PhotoImage(img8)

        Take_Attendance = Button(self.root, image=self.photoimage8, command=self.chatbot, cursor="hand2")
        Take_Attendance.place(x=512, y=500, width=180, height=180)

        b7 = Label(self.root, text="Chat Bot", cursor="hand2", font=("Garamond", 15, "bold"))
        b7.place(x=512, y=680, width=180, height=50)

        # Help
        img8 = Image.open("C:\\Users\\Rohan\\OneDrive\\Desktop\\Testing\\program_images\\help.png")
        img8 = img8.resize((200, 200))
        self.photoimage9 = ImageTk.PhotoImage(img8)

        Take_Attendance = Button(self.root, image=self.photoimage9, command=self.helpandsupport, cursor="hand2")
        Take_Attendance.place(x=200, y=500, width=180, height=180)

        b8 = Label(self.root, text="Help and support", cursor="hand2", font=("Garamond", 15, "bold"))
        b8.place(x=200, y=680, width=180, height=50)

    def open_second_window(self):
        self.second_window = Toplevel(self.root)
        self.app = addface(self.second_window)

    def mark_attendance(self, i, l, p, q, z):
        now = datetime.now()
        date_string = now.strftime("%d-%m-%Y")
        file_path = fr"C:\\Users\\Rohan\\OneDrive\\Desktop\\Testing\\Attendance\\Attendance_{date_string}.csv"

        if not os.path.exists(file_path):
            with open(file_path, "w", newline="\\n") as f:
                f.write("Name,Course,Year,Enrollment,Roll_no,Date,Time,Status\\n")

        with open(file_path, "r+", newline="\n") as f:
            myDatalist = f.readlines()
            name_list = []
            for line in myDatalist:
                entry = line.split(",")
                name_list.append(entry[0])

            if((i not in name_list) and (l not in name_list)):
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"{i},{l},{p},{q},{z},{date_string},{dtString},Present\\n")


    def f_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf, cursor):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coords = []
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), color, 3)

                enroll, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int(100 * (1 - predict / 300))

                # Fetch all data in one query
                cursor.execute("""
                    SELECT Name, Course, Year, Enrollment, Roll_no 
                    FROM student_data WHERE Attendance_id=%s
                """, (enroll,))
                row = cursor.fetchone()

                if row and confidence > 77:
                    name, course, year, enrollment, roll_no = row

                    # mark attendance only if student recognized with good confidence
                    self.mark_attendance(name, course, year, enrollment, roll_no)

                    cv2.putText(img, f"Name: {name}", (x, y-75),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (180,255,114), 2)
                    cv2.putText(img, f"Class: {course}", (x, y-50),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (180,255,114), 2)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0), 3)
                    cv2.putText(img, "Unknown Face", (x, y-30),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (180,255,114), 2)

                coords = [x, y, w, h]

            return coords

        def recognize(img, clf, faceCascade, cursor):
            coords = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf, cursor)
            return img

        # Load face cascade and trained classifier
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")   # ✅ case fixed

        # DB connection (only once, not per frame)
        conn = mysql.connector.connect(host="localhost", user="root", password="root", database="student_data")
        cursor = conn.cursor()

        video_cap = cv2.VideoCapture(0)
        while True:
            ret, img = video_cap.read()
            if not ret:
                break

            img = recognize(img, clf, faceCascade, cursor)
            cv2.imshow("Welcome to Face Recognition", img)

            # press Enter to break
            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()
        conn.close()

            
    def Attendance(self):
        self.scan = Toplevel(self.root)
        self.app = Attendance(self.scan)

    def programmers(self):
        self.scan = Toplevel(self.root)
        self.app = Developers(self.scan)

    def helpandsupport(self):
        self.scan = Toplevel(self.root)
        self.app = Helpandsupport(self.scan)

    def exit_button(self):
        result = messagebox.askquestion("Exit", "Are you Sure! You Want to quit window?")
        if result == "yes":
            root.destroy()
        else:
            return

    def chatbot(self):
        self.scan = Toplevel(self.root)
        self.app = Chatbot(self.scan)

    def read_pdf(self):
        pdf_file_path = "IJCRT2402465.pdf"  # Path to your PDF file

        # Create a new window to display PDF content
        pdf_window = Toplevel(self.root)
        pdf_window.title("PDF Viewer")
        pdf_window.geometry("800x600")

        # Create a text widget to display PDF content
        text_widget = Text(pdf_window, wrap=WORD, font=("Courier", 10))
        text_widget.pack(fill=BOTH, expand=YES)

        # Open and read the PDF file
        with open(pdf_file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text = page.extract_text()

                # Add spacing between pages
                if page_num > 0:
                    text_widget.insert(END, '\\n\\n')

                # Display the PDF content in the text widget
                text_widget.insert(END, text)

        # Disable text widget to make it non-editable
        text_widget.config(state=DISABLED)

                
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
