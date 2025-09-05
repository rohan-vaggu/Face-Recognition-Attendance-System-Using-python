from tkinter import Tk, Label
import tkinter
from PIL import Image, ImageTk
import sys

class Helpandsupport:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")
        root.configure(bg="lightblue")
        sys.setrecursionlimit(2000)

        bg_image = Image.open("C:\\Users\\Rohan\\OneDrive\\Desktop\\Testing\\program_images\\support_bg.png")
        bg_image = bg_image.resize((1530, 790), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tkinter.Label(self.root, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        tl1 = Label(root, text="HELP AND SUPPORT", font=("Garamond", 35, "bold"), fg="white", bg="black")
        tl1.place(x=320, y=30, width=1000, height=85)

        tl2 = Label(root, text="For any problem related Attendance System \n Contact or report poblem to \n following email or phone number: ", font=("Garamond", 20, "bold"), fg="black")
        tl2.place(x=320, y=100, width=1000, height=400)

        tl3 = Label(root, text="Email: rohanvaggu2416@gmail.com \n rutikmisal1982@gmail.com \n Contact: 8669061913 / 9822994330", font=("Garamond", 35, "bold"), fg="black")
        tl3.place(x=320, y=500, width=1000, height=200)

def main():
    win = Tk()
    app = Helpandsupport(win)
    win.mainloop()

if __name__ == "__main__":
    main()
