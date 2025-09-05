# 📸 Face Recognition Attendance System  

![Python](https://img.shields.io/badge/Python-3.10-blue)  
![OpenCV](https://img.shields.io/badge/OpenCV-LBPH-orange)  
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-yellow)  
![MySQL](https://img.shields.io/badge/Database-MySQL-brightgreen)  
![License](https://img.shields.io/badge/License-Educational-lightgrey)  

A **Python + OpenCV** based project that automates student attendance using real-time **face recognition**. The system detects and recognizes student faces, marks attendance in CSV/Database, and provides a **Tkinter GUI** with modules for Login, Registration, Chatbot, Help, and more.  

---

## 🚀 Features
- 👤 **Face Detection & Recognition** using Haar Cascades + LBPH algorithm  
- 📝 **Automatic Attendance Logging** (CSV + Database) with date/time  
- 🔐 **Authentication System**  
  - User Login & Registration  
  - Password Recovery (via Security Questions)  
- 🖼️ **Tkinter GUI** with multi-window navigation  
- 📊 **Student Management** (Add, Update, Delete, Train faces)  
- 🤖 **Simple Chatbot** for FAQs  
- 👨‍💻 **Developers Page & Help Section**  
- 📂 Organized dataset: `Face_Dataset/` and attendance logs in `Attendance/`  

---

## 🛠️ Tech Stack
- **Language:** Python  
- **Libraries:** OpenCV, Tkinter, Pillow, Pandas  
- **Database:** MySQL (`mysql-connector-python`)  
- **Model:** LBPH Face Recognizer (OpenCV)  

---

## 📂 Project Structure
- face-recognition-attendance/
  - │── app.py # Entry point (launches Login window)
  - │── main.py # Main dashboard after login
  - │── login.py # Login window
  - │── register.py # Registration window
  - │── forgetpass.py # Password reset
  - │ ── addface.py # Add student & train faces
  - │── attendance.py # Attendance viewer
  - │── chatbot.py # Chatbot module
  - │── developers.py # About developers
  - │── helpandsupport.py # Help & support window
  - │── utils.py # Helper functions (paths, hashing)
  - │── db.py # MySQL connection + schema
  - │── assets/ # Haar cascade, icons, background images
  - │── Face_Dataset/ # Captured student images
  - │── Attendance/ # Attendance CSV logs
  - │── requirements.txt # Python dependencies
  - │── README.md # Project documentation



---

## ⚙️ Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/face-recognition-attendance.git
   cd face-recognition-attendance


## Create Database

`SQL`

```
CREATE DATABASE student_data;
USE student_data;

CREATE TABLE regteach (
    fname VARCHAR(50),
    lname VARCHAR(50),
    cnum VARCHAR(20),
    email VARCHAR(100) PRIMARY KEY,
    ssq VARCHAR(150),
    sa VARCHAR(150),
    pwd VARCHAR(100)
);

CREATE TABLE student_data (
    Attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    Enrollment VARCHAR(50) UNIQUE,
    Roll_no VARCHAR(20),
    Name VARCHAR(100),
    Course VARCHAR(50),
    Year VARCHAR(20),
    Division VARCHAR(10)
);

```

## 📜 License

This project is for educational purposes only.
You are free to modify and use it for learning.
