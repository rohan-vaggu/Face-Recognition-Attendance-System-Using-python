from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import sys

class Developers:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("About Developers")
        sys.setrecursionlimit(2000)
        
        bg_image = Image.open("C:\\Users\\Rohan\\OneDrive\\Desktop\\Testing\\program_images\\bvp.jpg")
        bg_image = bg_image.resize((1530, 790), Image.LANCZOS)  # Changed from Image.ANTIALIAS
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(self.root, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        title_label = tk.Label(self.root, text="About Developers", font=("Garamond", 35, "bold"), bg="white", fg="black")
        title_label.place(x=0, y=30, width=1530, height=85)

        img1 = Image.open("C:\\Users\\Rohan\\OneDrive\\Desktop\\Testing\\program_images\\kanak.jpg")
        img1 = img1.resize((200, 200), Image.LANCZOS)  # Changed from Image.ANTIALIAS
        self.photoimage1 = ImageTk.PhotoImage(img1)

        Kanak = tk.Button(self.root, image=self.photoimage1, cursor="hand2")
        Kanak.place(x=200, y=200, width=180, height=180)

        b1 = tk.Label(self.root, text="Kanak Hiran", font=("Garamond", 15, "bold"), bg="lightblue")
        b1.place(x=200, y=380, width=180, height=50)

        img2 = Image.open("C:\\Users\\Rohan\\OneDrive\\Desktop\\Testing\\program_images\\Rutik.jpg")
        img2 = img2.resize((200,200), Image.LANCZOS)  # Changed from Image.ANTIALIAS
        self.photoimage2 = ImageTk.PhotoImage(img2)

        rutik= Button(self.root,image=self.photoimage2, cursor="hand2")
        rutik.place(x=512, y=200, width=180, height=180)

        b2 = Label(self.root,text="Rutik Misal", cursor="hand2",font=("Garamond",15,"bold"))
        b2.place(x=512, y=380, width=180, height=50)

        img3 = Image.open("C:\\Users\\Rohan\\OneDrive\\Desktop\\Testing\\program_images\\Rohan.jpg")
        img3 = img3.resize((200,200), Image.LANCZOS)  # Changed from Image.ANTIALIAS
        self.photoimage3 = ImageTk.PhotoImage(img3)

        Rohan= Button(self.root,image=self.photoimage3 ,cursor="hand2")
        Rohan.place(x=825, y=200, width=180, height=180)

        b3 = Label(self.root,text="Rohan Vaggu", cursor="hand2",font=("Garamond",15,"bold"))
        b3.place(x=825, y=380, width=180, height=50)

        img4 = Image.open("C:\\Users\\Rohan\\OneDrive\\Desktop\\Testing\\program_images\\suyash.png")
        img4 = img4.resize((200,200), Image.LANCZOS)  # Changed from Image.ANTIALIAS
        self.photoimage4 = ImageTk.PhotoImage(img4)

        Suyash = Button(self.root,image=self.photoimage4,cursor="hand2")
        Suyash.place(x=1150, y=200, width=180, height=180)

        b4 = Label(self.root,text="Suyash Waykar", cursor="hand2",font=("Garamond",15,"bold"))
        b4.place(x=1150, y=380, width=180, height=50)

if __name__ == "__main__":
    root = Tk()
    obj=Developers(root)
    root.mainloop()