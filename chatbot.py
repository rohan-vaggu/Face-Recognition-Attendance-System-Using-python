from tkinter import *
from tkinter import ttk
import sys

class Chatbot:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")
        root.configure(bg="lightblue")
        sys.setrecursionlimit(2000)

        self.var_question = StringVar()

        chatbox = LabelFrame(root, bd=2, relief=RIDGE, text="Chat Bot", font=("Garamond", 14, "bold"), fg="red")
        chatbox.place(x=200, y=5, width=1150, height=800)

        self.chat_history = Text(chatbox, bd=1, relief=RIDGE, font=("Arial", 12), wrap=WORD, state='disabled')
        self.chat_history.place(x=10, y=10, width=1130, height=680)

        qn = ttk.Combobox(chatbox, state="readonly", width=25, textvariable=self.var_question)
        qn["values"] = ("Select Question", "How does facial recognition works", "What is machine learning",
                        "What is your name?", "what is python programming",
                        "Where we can use face recognition system?",
                        "why face recognition attendance system is better than manual attendance system?",
                        "What is Advantage and disadvantage of face recognition attendance system?",
                        "Who created you?")
        qn["font"] = ("Arial", 15)
        qn.current(0)
        qn.place(x=10, y=700, width=800, height=30)

        send = Button(chatbox, width=20, font=("Arial", 15, "bold"), text="Send", bg="blue", fg="white",
                      command=self.send_message)
        send.place(x=850, y=700, width=100, height=30)

        clear_btn = Button(chatbox, width=20, font=("Arial", 15, "bold"), text="Clear Chat", bg="red", fg="white",
                           command=self.clear_chat)
        clear_btn.place(x=970, y=700, width=150, height=30)

        self.responses = {
            "How does facial recognition works": "Facial recognition works by identifying and verifying a person's "
                                                  "identity using their facial features. It typically involves capturing "
                                                  "an image or video of a person's face, analyzing it to extract "
                                                  "distinctive features, and comparing those features against a database "
                                                  "of known faces.",
            "What is machine learning": "Machine learning is a subset of artificial intelligence (AI) that focuses on "
                                        "the development of algorithms and models that allow computers to learn and "
                                        "make predictions or decisions based on data without being explicitly programmed. "
                                        "It enables computers to improve their performance on a task as they are "
                                        "exposed to more data over time.",
            "What is your name?": "I'm a chatbot designed to answer questions related to facial recognition attendance "
                                  "systems. You can ask me anything!",
            "what is python programming": "Python is a high-level, interpreted programming language known for its "
                                          "simplicity and readability. It is widely used in various domains such as web "
                                          "development, data analysis, artificial intelligence, and more.",
            "Where we can use face recognition system?": "Face recognition systems can be used in various applications "
                                                        "including school or collage attendance system, "
                                                        "attendance tracking, user authentication, and more.",
            "why face recognition attendance system is better than manual attendance system?": "Face recognition "
                                                                                                "attendance systems "
                                                                                                "offer several "
                                                                                                "advantages over "
                                                                                                "manual systems "
                                                                                                "including "
                                                                                                "automation, "
                                                                                                "accuracy, "
                                                                                                "elimination of "
                                                                                                "buddy punching, "
                                                                                                "and convenience.",
            "What is Advantage and disadvantage of face recognition attendance system?": "The advantages of face "
                                                                                          "recognition attendance "
                                                                                          "systems include "
                                                                                          "accurate identification, "
                                                                                          "time efficiency, and "
                                                                                          "security. However, "
                                                                                          "disadvantages may "
                                                                                          "include privacy concerns "
                                                                                          "and potential errors in "
                                                                                          "recognition.",
            "Who created you?": "I have created by developer Rohan Vaggu"
        }

    def send_message(self):
        question = self.var_question.get()
        answer = self.responses.get(question, "Sorry, I don't understand that question.")
        self.chat_history.config(state='normal')
        self.chat_history.insert(END, f"\nYou: {question}\nBot: {answer}\n")
        self.chat_history.config(state='disabled')

    def clear_chat(self):
        self.chat_history.config(state='normal')
        self.chat_history.delete(1.0, END)
        self.chat_history.config(state='disabled')

if __name__ == "__main__":
    root = Tk()
    obj = Chatbot(root)
    root.mainloop()
