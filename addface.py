from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from PIL import Image
import sys

class addface:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Online Face Recognition System")
        root.configure(bg="lightblue")
        sys.setrecursionlimit(2000)
        
        #Variables
        self.var_attend_id = StringVar()
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_Cource = StringVar()
        self.var_Year = StringVar()
        self.var_division = StringVar()
        self.var_enrollment = StringVar()

        #Heading lable
        tl2 = Label(root, text="Student  Data", font=("Aptos Display",50),bg="lightblue")
        tl2.place(x=0, y=10, width=1500, height=100)

        #Create main frame
        main_fram = Frame(root,bd=2)
        main_fram.place(x=5, y=100, width=1525, height=685)

        #Lable_frame left
        Left_fram = LabelFrame(main_fram,bd=2,relief=RIDGE,text="Input Student Details",font=("Garamond",14,"bold"),fg="red")
        Left_fram.place(x=10, y=10, width=750, height=655)

        #Lable_frame Right
        Right_fram = LabelFrame(main_fram,bd=2,relief=RIDGE,text="Total Students Data",font=("Garamond",14,"bold"),fg="red")
        Right_fram.place(x=780, y=10, width=725, height=655)

        #table Frame
        Scroll_x = ttk.Scrollbar(Right_fram, orient=HORIZONTAL)
        Scroll_y = ttk.Scrollbar(Right_fram, orient=VERTICAL)

        self.student_table = ttk.Treeview(Right_fram,column=("Attendance id","Enrollment","Roll Number","Name","Cource","Year","Division"),xscrollcommand=Scroll_x.set, yscrollcommand=Scroll_y.set)

        Scroll_x.pack(side=BOTTOM, fill=X)
        Scroll_y.pack(side=RIGHT, fill=Y)

        Scroll_x.config(command=self.student_table.xview)
        Scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Attendance id", text="Attendance id")
        self.student_table.heading("Enrollment", text="Enrollment Number")
        self.student_table.heading("Name", text="Namer")
        self.student_table.heading("Roll Number", text="Roll Number")
        self.student_table.heading("Cource", text="Cource")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Division", text="Division")
        self.student_table["show"]="headings"

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        

        #Studen details
        #Name
        serial = Label(Left_fram,text="Attendance id:",font=("Garamond",15))
        serial.grid(row=0, column=0)

        serialE = Entry(Left_fram,textvariable=self.var_attend_id,width=27,font=("Garamond",15))
        serialE.grid(row=0, column=1)

        a = Label(Left_fram,text="")
        a.grid(row=1, column=0)

        b = Label(Left_fram,text="")
        b.grid(row=1, column=0)

        name = Label(Left_fram,text="Name",font=("Garamond",15))
        name.grid(row=2, column=0)

        name1 = Entry(Left_fram,textvariable=self.var_name,width=27,font=("Garamond",15))
        name1.grid(row=2, column=1)
        
        #Department
        b = Label(Left_fram,text="")
        b.grid(row=3,column=0)

        depart = Label(Left_fram,text="Department ",font=("Garamond",15))
        depart.grid(row=4,column=0)

        #Year
        c = Label(Left_fram,text="")
        c.grid(row=5,column=0)

        year = Label(Left_fram,text="Education Year ",font=("Garamond",15))
        year.grid(row=6,column=0)

        #Roll number
        d = Label(Left_fram,text="")
        d.grid(row=7,column=0)

        roll_no = Label(Left_fram,text="Roll number ",font=("Garamond",15))
        roll_no.grid(row=8,column=0)
        
        #department combobox
        dep_combo = ttk.Combobox(Left_fram, width=25, textvariable=self.var_Cource, state="readonly")
        dep_combo["values"] = ("Select Branch", "Computer", "Mechanical", "Civil", "Chemical")
        dep_combo["font"] = ("Garamond", 15)
        dep_combo.current(0)
        dep_combo.grid(row=4, column=1)

        year_comb = ttk.Combobox(Left_fram, textvariable=self.var_Year, width=25, font=("Garamond", 15), state="readonly")
        year_comb["values"] = ("Select Year", "First year", "Second Year", "Third Year")
        year_comb.current(0)
        year_comb.grid(row=6, column=1)

        #Division combobox

        blank_lable = Label(Left_fram,text="",font=("Garamond",15))
        blank_lable.grid(row=11, column=0)

        div_comb = ttk.Combobox(Left_fram,textvariable=self.var_division,width=25,font=("Garamond",15),state="readonly")
        div_comb["values"]=("Select division","A","B")
        div_comb.current(0)
        div_comb.grid(row=12,column=1)

        b_lable = Label(Left_fram,text="",font=("Garamond",15))
        b_lable.grid(row=12, column=0)

        div_lable = Label(Left_fram,text="Division",font=("Garamond",15))
        div_lable.grid(row=12, column=0)

        #Roll number box
        roll_no = Entry(Left_fram,width=27,textvariable=self.var_roll,font=("Garamond",15))
        roll_no.grid(row=8, column=1)

        blank_lable2 = Label(Left_fram,text="")
        blank_lable2.grid(row=13, column=0)

        #Enrollment number
        Enroll_lable = Label(Left_fram,text="Enrollment number:",font=("Garamond",15))
        Enroll_lable.grid(row=14, column=0)
        Enrollment_no = Entry(Left_fram,width=27,textvariable=self.var_enrollment,font=("Garamond",15))
        Enrollment_no.grid(row=14, column=1)

        #blank space
        blank_lable3 = Label(Left_fram,text="")
        blank_lable3.grid(row=15, column=0)

        save = Button(Left_fram,width=20,font=("Garamond",15,"bold"),command=self.add_face,text="Save",bg="blue",fg="white")
        save.grid(row=16, column=0,padx=5,pady=5)

        update = Button(Left_fram,width=20,font=("Garamond",15,"bold"),command=self.get_update,text="Update",bg="blue",fg="white")
        update.grid(row=16, column=1,padx=5,pady=5)
        
        Delete = Button(Left_fram,width=17,font=("Garamond",15,"bold"),command=self.delete_data,text="Delete",bg="blue",fg="white")
        Delete.grid(row=16, column=2,padx=5,pady=5)
        
        photo_sample = Button(Left_fram,width=20,height=1,font=("Garamond",15,"bold"),command=self.create_dataset,text="Add photo sample",bg="blue",fg="white")
        photo_sample.grid(row=17, column=0,padx=5,pady=5)

        Reset = Button(Left_fram,width=17,height=1,font=("Garamond",15,"bold"),command=self.reset_data,text="Reset",bg="blue",fg="white")
        Reset.grid(row=17, column=2,padx=5,pady=5)

        Train = Button(Left_fram,width=20,height=1,font=("Garamond",15,"bold"),command=self.train_classifier,text="Create xml file",bg="blue",fg="white")
        Train.grid(row=17, column=1,padx=5,pady=5)

    
    def add_face(self):
        if self.var_attend_id.get()=="" or self.var_roll.get()=="" or self.var_name.get()=="" or self.var_Cource.get()=="" or self.var_Year.get()=="" or self.var_division.get()=="":
            messagebox.showerror("Error","All Feilds Are Require",parent = self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password = "root", database="Student_data")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student_data values(%s, %s, %s, %s, %s, %s,%s)",(
                                                                                        self.var_attend_id.get(),
                                                                                        self.var_enrollment.get(),
                                                                                        self.var_roll.get(),
                                                                                        self.var_name.get(),
                                                                                        self.var_Cource.get(),
                                                                                        self.var_Year.get(),
                                                                                        self.var_division.get()
                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Successfully Added")

            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)



    #fetch database data
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password = "root", database="Student_data")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student_data")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #Edit details
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_attend_id.set(data[0]),
        self.var_enrollment.set(data[1]),
        self.var_roll.set(data[2]),
        self.var_name.set(data[3]),
        self.var_Cource.set(data[4]),
        self.var_Year.set(data[5]),
        self.var_division.set(data[6])

    #update data function
    def get_update(self):
        if self.var_attend_id.get()=="" or self.var_enrollment.get()=="" or self.var_roll.get()=="" or self.var_name.get()=="" or self.var_Cource.get()=="Select Branch" or self.var_Year.get()=="Select Year" or self.var_division.get()=="Select division":
            messagebox.showerror("Error","All Feilds Are Require",parent = self.root)

        else:
            try:
                update_msg = messagebox.askyesno("Update","Do you want to update student details?",parent = self.root)
                if update_msg>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password = "root", database="Student_data")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student_data set Attendance_id=%s,roll_no=%s, Name=%s, Course=%s, Year=%s, Division=%s where Enrollment=%s",(
                                                                                                                            self.var_attend_id.get(),
                                                                                                                            self.var_roll.get(),
                                                                                                                            self.var_name.get(),                                                                                                                    
                                                                                                                            self.var_Cource.get(),
                                                                                                                            self.var_Year.get(),
                                                                                                                            self.var_division.get(),                                                        
                                                                                                                            self.var_enrollment.get()
                                                                                                                        ))
                    
                else:
                    if not update_msg:
                        return      
                messagebox.showinfo("Success","Student detail successfully updated", parent = self.root)
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent = self.root)


    #Delete button function
    def delete_data(self):
        if self.var_roll.get()=="":
            messagebox.showerror("Error","Student Roll number require")
        else:
            try:
                delete = messagebox.askyesno("student delete page","Do you want to delete student detail?")
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password = "root", database="Student_data")
                    my_cursor=conn.cursor()
                    sql = "delete from student_data where Enrollment=%s"
                    val=(self.var_enrollment.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted")

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent = self.root)

    def reset_data(self):
        self.var_attend_id.set("")
        self.var_enrollment.set("")
        self.var_roll.set("")
        self.var_Cource.set("Select Branch")
        self.var_name.set("")
        self.var_Year.set("Select Year")
        self.var_division.set("Select division")

    #Take Face photo sample
    def create_dataset(self):
        if self.var_enrollment.get()=="" or self.var_roll.get()=="" or self.var_name.get()=="" or self.var_Cource.get()=="Select Branch" or self.var_Year.get()=="Select Year" or self.var_division.get()=="Select division":
            messagebox.showerror("Error","All Feilds Are Require",parent = self.root)

        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password = "root", database="Student_data")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student_data")
                my_result = my_cursor.fetchall()
                id = 0
                for x in my_result:
                    id += 1
                my_cursor.execute("update student_data set Attendance_id=%s, roll_no=%s, Name=%s, Course=%s, Year=%s, Division=%s where Enrollment=%s",  (
                                                                                                                            self.var_attend_id.get(),
                                                                                                                            self.var_roll.get(),                                                                                                                            
                                                                                                                            self.var_name.get(),                                                                                                                    
                                                                                                                            self.var_Cource.get(),
                                                                                                                            self.var_Year.get(),
                                                                                                                            self.var_division.get(),                                                        
                                                                                                                            self.var_enrollment.get()==id+1
                                                                                                                        ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #face classifier
                
                face_clssifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_clssifier.detectMultiScale(gray,1.5,5)

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret,my_Frame=cap.read()
                    if face_cropped(my_Frame) is not None:
                        img_id+=1
                        face = cv2.resize(face_cropped(my_Frame),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = "Face_Dataset//user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()

                messagebox.showinfo("Result","Generating Dataset completed")
            
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent = self.root)
    
    def train_classifier(self):
        data_dir=("Face_Dataset")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        
     
        for image in path:
            img = Image.open(image).convert('L')
            imageNp = np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13

        ids = np.array(ids)
        
        #Train classifier
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("result","Training dataset completed")
    
if __name__ == "__main__":
    root = Tk()
    obj=addface(root)
    root.mainloop()